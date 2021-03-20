"""
This program is to send automatic message to the users which 
are present in redis database

"""

import os
import requests
import redis
import time


#connect to redis

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)

# fetch the chat ids of all the users from list

db_keys = set(map(int,redisClient.smembers("userset")))

# print(type(db_keys[0]))


# enter your bot token at the place of TOKEN
bot_token = '<TOKEN>'

#function to send message to user
def send_announcments(bot_message):
    for keys in db_keys:
        print(keys)
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(keys) + '&text=' + bot_message
        print(send_text)
        response = requests.get(send_text)
        print (response.json())
        time.sleep(1)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bot_message = open (os.path.join(__location__, "message_bot.txt"))

text_content = bot_message.read()

while True:
    send_announcments(bot_message = text_content)

    time.sleep(60)