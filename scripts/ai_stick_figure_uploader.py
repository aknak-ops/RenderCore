from openai import OpenAI
import os
import requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# === Google Drive Auth ===
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# === AI Image Generation ===
def generate_stick_figure():
    client = OpenAI()
    prompt = "Simple stick figure standing, plain background"
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    url = response.data[0].url

    os.makedirs("test", exist_ok=True)
    image_path = "test/test_stick_figure.png"
    with open(image_path, "wb") as f:
        f.write(requests.get(url).content)
    return image_path

# === Upload to Google Drive ===
def upload_file(service, file_path, folder_id=None):
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    media = MediaFileUpload(file_path, mimetype='image/png')
    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f"Uploaded file with ID: {uploaded_file.get('id')}")

# === Run ===
if __name__ == "__main__":
    file_path = "test/test_stick_figure.png"
    if not os.path.exists(file_path):
        print("File not found, generating one...")
        file_path = generate_stick_figure()
    upload_file(service, file_path)
