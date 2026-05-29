import os


def require_env(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


DISCORD_TOKEN: str = require_env("DISCORD_TOKEN")
SECRET_CHANNEL_ID: int = int(require_env("SECRET_CHANNEL_ID"))
