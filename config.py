class Config:
    """Config class for variables."""

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
SUDO_USERS = int(os.environ.get("SUDO_USERS", ""))
DEV_USERS = int(os.environ.get("DEV_USERS", ""))
BOT_NAME = os.environ.get("BOT_NAME", "")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")

class Local:
    """Config class for variables."""

LOG_CHANNEL = -1001182935463
BOT_TOKEN = 123456:jsd9rh443fh9dvs
APP_ID = 192803
API_HASH = hd82828h2872tw02
BOT_USERNAME = MissTanuBot
OWNER_ID = 1182935463
SUDO_USERS = 1182935463
DEV_USERS = 1182935463
BOT_NAME = Tanu
SUPPORT_GROUP = RhythmOff
UPDATES_CHANNEL = RhythmOfficial