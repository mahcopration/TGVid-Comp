import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "10917377")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "22bfe49f4482c5cb5424729249a5f097") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7064479547:AAGUOtEwRxad3xY7E78B5A48TWenQPsGIuU") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Call_me_futurepilot') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://videoencodemass:videoencodemass@cluster0.yns1vfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","VideoEncoderFastBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6112399514")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002088909747')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
