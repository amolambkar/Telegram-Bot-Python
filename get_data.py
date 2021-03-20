import json 
import requests
import redis

TOKEN = "<TOKEN>"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    first_name = updates["result"][last_update]["message"]["chat"]["first_name"]
    last_name = updates["result"][last_update]["message"]["chat"]["last_name"]
    return (text, chat_id,first_name,last_name)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
def get_data():

    text, chat , first_name , last_name = get_last_chat_id_and_text(get_updates())
    # send_message(text, chat)
    print(text, chat,first_name,last_name)

    name = first_name +" "+ last_name

    redisClient = redis.StrictRedis(host='localhost',

                                    port=6379,

                                    db=0)

    redisClient.hset("user", name, chat)

    redisClient.sadd("userset",chat)

    db_keys = redisClient.hgetall("user")

    print(db_keys)

get_data()