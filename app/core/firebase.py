from pathlib import Path

import firebase_admin

from firebase_admin import credentials


SERVICE_ACCOUNT_PATH = (
    Path(__file__).resolve().parents[1]
    / "secrets"
    / "cinepulseapp-f6398-firebase-adminsdk-fbsvc-be60bfa73e.json"
)


def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(str(SERVICE_ACCOUNT_PATH))
        return firebase_admin.initialize_app(cred)