import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "CC_M9")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Kareemalfehr/MR_X_MUSIC-Video")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CC_M9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CC_M9")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1902951996").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ت م ا غ س ش ك").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/bf9a015adf25f828f298a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("https://telegra.ph/file/eeb03face4f5ae4d0f76a.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
