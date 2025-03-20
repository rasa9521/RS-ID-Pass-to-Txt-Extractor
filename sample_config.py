import os

api_id = 25364269
api_hash = os.environ.get("API_HASH", "ddfbbd94cf441e22ee71bb7f4695c2f1")
bot_token = os.environ.get("BOT_TOKEN", "7906984827:AAHK9VXO1oDKCD3f-HfJlL8xnWF4wuE0wiM")
auth_users = os.environ.get("AUTH_USERS", "2093417522")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "2093417522")
owner_users = [int(num) for num in osowner_users.split("2093417522")]
