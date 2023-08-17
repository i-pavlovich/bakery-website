from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Config()
