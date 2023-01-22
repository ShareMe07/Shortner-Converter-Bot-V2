# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24862026"))
API_HASH = os.environ.get("API_HASH", "cc816e78e7084155e360976c52ca08dd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800276525:AAE5kJnEVgYxVh3qF62KHahVMXFEavflK2I")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5890495617")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskShortners")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://00998855:Mfh@9066@cluster0.bylasy0.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5890495617")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
