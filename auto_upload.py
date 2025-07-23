import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Configuration: change as needed
RENDER_ROOT = "."  # Folder where your render zips live
TARGET_DRIVE_FOLDER_NAME = "RenderCore_Exports"  # Drive folder to upload into

def authenticate_drive():
    gauth = GoogleAuth()
    # Try to load saved credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if no saved credentials
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    print("[OK] Authenticated and ready to use Google Drive API.")
    return drive

def get_or_create_folder(drive, folder_name):
    # Query for existing folder
    file_list = drive.ListFile({'q': f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    if file_list:
        folder_id = file_list[0]['id']
        print(f"[OK] Found existing Drive folder '{folder_name}' (ID: {folder_id})")
        return folder_id
    # Create new folder if not found
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    print(f"[OK] Created new Drive folder '{folder_name}' (ID: {folder['id']})")
    return folder['id']

def find_latest_zip(folder_path):
    zips = [f for f in os.listdir(folder_path) if f.lower().endswith(".zip")]
    if not zips:
        print(f"[ERROR] No .zip files found in {folder_path}")
        return None
    # Sort by modified time, descending (latest first)
    zips.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)
    latest = zips[0]
    print(f"[OK] Found latest zip: {latest}")
    return latest

def upload_file_to_drive(drive, folder_id, filepath):
    file_name = os.path.basename(filepath)
    print(f"[INFO] Uploading '{file_name}' to Drive folder ID {folder_id} ...")
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
    gfile.SetContentFile(filepath)
    gfile.Upload()
    print(f"[SUCCESS] Uploaded '{file_name}' with file ID: {gfile['id']}")
    # Return a shareable link
    permission = gfile.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'
    })
    share_url = f"https://drive.google.com/file/d/{gfile['id']}/view?usp=sharing"
    print(f"[LINK] File available at: {share_url}")
    return share_url

def main():
    try:
        drive = authenticate_drive()
    except Exception as e:
        print(f"[ERROR] Authentication failed: {e}")
        sys.exit(1)

    folder_id = get_or_create_folder(drive, TARGET_DRIVE_FOLDER_NAME)
    latest_zip = find_latest_zip(RENDER_ROOT)
    if not latest_zip:
        print("[ERROR] No zip to upload, exiting.")
        sys.exit(1)

    zip_path = os.path.join(RENDER_ROOT, latest_zip)
    try:
        upload_file_to_drive(drive, folder_id, zip_path)
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
