from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SpeechTrain"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    groq_api_key: str = ""
    groq_text_model: str = "llama-3.3-70b-versatile"
    groq_transcription_model: str = "whisper-large-v3-turbo"
    croo_private_key: str = ""
    croo_api_url: str = "https://api.croo.network"
    croo_ws_url: str = "wss://network.croo.network"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
