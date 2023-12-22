import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 14911221))

    API_HASH = os.environ.get("API_HASH", "a5e14021456afd496e7377331e2e5bcf")
