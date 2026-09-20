import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # Telegram API ki ID
    API_ID = int(os.environ.get("API_ID", "0"))
    # Telegram API hash
    API_HASH = os.environ.get("API_HASH", "")
    ADMIN_ID = [int(x) for x in os.environ.get("ADMIN_ID", "0").split(",")]
    # Bot ke owner ka Telegram user ID (for send_message)
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    # MongoDB database ka URL
    DB_URL = os.environ.get("DB_URL", "")
    # Database ka naam
    DB_NAME = os.environ.get("DB_NAME", "master_extractor")
    # Text log channel ki ID (currently unused by any module -- reserved)
    TXT_LOG = int(os.environ.get("TXT_LOG", "0"))
    # Authentication log channel ki ID
    AUTH_LOG = int(os.environ.get("AUTH_LOG", "0"))
    # Hit log channel ki ID (currently unused by any module -- reserved)
    HIT_LOG = int(os.environ.get("HIT_LOG", "0"))
    # DRM dump channel ki ID (currently unused by any module -- reserved)
    DRM_DUMP = int(os.environ.get("DRM_DUMP", "0"))
    # Main channel ki ID (used for force-subscribe check)
    CHANNEL = int(os.environ.get("CHANNEL", "0"))
    # Channel ka link
    CH_URL = os.environ.get("CH_URL", "https://t.me/")
    # Bot ke owner ka Telegram link
    OWNER = os.environ.get("OWNER", "https://t.me/")
    # Thumbnail image ka URL
    THUMB_URL = os.environ.get("THUMB_URL", "https://telegra.ph/file/example-thumb-image.jpg")
    # Premium logs channel (same as CHANNEL by default)
    PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "0"))
    # Channel IDs used by module extractors (currently unused by any module -- reserved)
    CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
    CHANNEL_ID2 = os.environ.get("CHANNEL_ID2", "")
    # Bot display text
    BOT_TEXT = os.environ.get("BOT_TEXT", "Master Extractor")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MasterExtractorBot")
    # API host ka URL
    HOST = os.environ.get("HOST", "https://api.masterapi.tech")
