import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = '5780148364:AAFcCHgzhaIDj_cNUBOpSglQsADnHAnsCeE'

APP_ID = 2419770

API_HASH = 'eec8bf9b714bc4942e1cbfbdfb299063'

CHANNEL_ID = '-1001874504630'

OWNER_ID = '1602757268'

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get(
    "START_MESSAGE", "Привет {firstname}\n\nI помогу создать приватную ссылку на файлы для твоего канала")
try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception(
        "Your list of administrators does not contain permissible integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(1602757268)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
