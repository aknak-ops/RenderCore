import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_folder(local_folder, drive_folder_id):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.json")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("credentials.json")

    drive = GoogleDrive(gauth)
    for filename in os.listdir(local_folder):
        f = drive.CreateFile({'title': filename, 'parents': [{'id': drive_folder_id}]})
        f.SetContentFile(os.path.join(local_folder, filename))
        f.Upload()
        print(f"Uploaded: {filename}")
