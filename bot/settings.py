from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    twitch_channels: list[str]
    twitch_prefix: str = "!"
    twitch_token: str
    discord_prefix: str = "!"
    discord_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
