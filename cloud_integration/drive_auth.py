
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # opens browser
    drive = GoogleDrive(gauth)
    print("[OK] Authenticated and ready to use Google Drive API.")
    return drive

if __name__ == "__main__":
    authenticate()
