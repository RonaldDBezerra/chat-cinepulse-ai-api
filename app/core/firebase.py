import firebase_admin
from firebase_admin import credentials

from app.core.config import settings


def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(settings.firebase_credentials)
        return firebase_admin.initialize_app(cred)