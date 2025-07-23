
from drive_auth import authenticate
import os

def upload_file(filepath, parent_id=None):
    drive = authenticate()
    file_name = os.path.basename(filepath)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': parent_id}]} if parent_id else {'title': file_name})
    gfile.SetContentFile(filepath)
    gfile.Upload()
    print(f"[OK] Uploaded: {file_name}")

if __name__ == "__main__":
    upload_file("Barbell_Bicep_Curl_bundle.zip")
