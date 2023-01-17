import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "9187528")

API_HASH = os.environ.get("API_HASH", "26e7cef4bad59d61a9cca5e600bce2a2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5907234159:AAEGoPbnXPp7OG6INPiZyTEVSPdMzRY8VN8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001880118183) 

DB_NAME = os.environ.get("DB_NAME","Skin")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://skin:skin2580@cluster0.wa1rae0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/8e86ae81d18c609a20810.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5570339899').split()]

PORT = os.environ.get("PORT", "8080")
