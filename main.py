from telethon.sync import TelegramClient
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER, API_ID, API_HASH
import mysql.connector


# with mysql.connector.connect(database=DATABASE_NAME, user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD) as connection:
#     with connection.cursor() as cursor:
#         sql = f"SHOW TABLES"
#         cursor.execute(sql)
#         tables = cursor.fetchall()
#         for table in tables:
#             print(table[0])
#     connection.commit()


client = TelegramClient('session', api_id=API_ID, api_hash=API_HASH)
client.start()
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

my_user  = client.send_message(136724293, "hi")
print(my_user)
