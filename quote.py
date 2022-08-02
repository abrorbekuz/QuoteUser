from pyrogram import Client
from QuoteMaker.QuoteMaker import QUOTE
from config import details
import time

client = Client( **details ).start()
quote = QUOTE(size=(800, 800))

last_time = ''

def Is_Updated(last_time):
    now_time = time.strftime('%H:%M')
    if now_time != last_time:
        quote.create_image()
    return now_time, last_time != now_time

while True:
    last_time, update = Is_Updated(last_time)
    if update:
        photos = list(client.get_chat_photos('me'))
        client.delete_profile_photos(photos[0].file_id)
        client.set_profile_photo(photo="image.jpg")
        print("updated")
    