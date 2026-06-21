import base64
import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str

    # TMDB
    TMDB_API_KEY: str

    # LangSmith (observabilidade/tracing)
    LANGSMITH_TRACING: bool = False
    LANGSMITH_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGSMITH_API_KEY: str | None = None
    LANGSMITH_PROJECT: str | None = None

    # Database (Postgres / Supabase - usado como checkpointer do LangGraph)
    DATABASE_URL: str

    # Firebase Admin SDK (service account em base64)
    FIREBASE_CREDENTIALS_BASE64: str

    # Certificado SSL do banco (CA do Supabase) em base64
    DB_SSL_CERT_BASE64: str | None = None

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".env"),
        extra="ignore",
    )

    @property
    def firebase_credentials(self) -> dict:
        decoded = base64.b64decode(self.FIREBASE_CREDENTIALS_BASE64)
        return json.loads(decoded)

    @property
    def db_ssl_cert_path(self) -> str | None:
        if not self.DB_SSL_CERT_BASE64:
            return None

        decoded = base64.b64decode(self.DB_SSL_CERT_BASE64)
        cert_path = Path("/tmp/prod-ca-2021.crt")
        cert_path.write_bytes(decoded)
        cert_path.chmod(0o600)
        return str(cert_path)

    @property
    def database_conn_string(self) -> str:
        if not self.db_ssl_cert_path:
            return self.DATABASE_URL

        parsed = urlparse(self.DATABASE_URL)
        query = dict(parse_qsl(parsed.query))
        query["sslmode"] = "verify-full"
        query["sslrootcert"] = self.db_ssl_cert_path
        return urlunparse(parsed._replace(query=urlencode(query)))


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()