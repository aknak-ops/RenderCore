import os
import pickle
import mimetypes
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def upload_file(service, file_path, folder_id=None):
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    mime_type, _ = mimetypes.guess_type(file_path)
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print(f"Uploaded: {file_path} → File ID: {file.get('id')}")

if __name__ == "__main__":
    service = authenticate()
    # CHANGE THIS to your test file path and Drive folder ID if needed
    upload_file(service, "test/test_stick_figure.png", folder_id=None)