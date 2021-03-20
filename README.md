# Telegram-Bot-Python
Bot to send periodic updates and reply to telegram user using python with Redis Database.

Python Telegram Bot

Total Files -

1 - bot.py
2 - get_data.py
3 - update.py
---------------------------------------------------------------------------

on the redis-server first
---------------------------------------------------------------------------

In every file please enter "token of your bot" at place of <TOKEN>

    -- change on line 59 and line 83 in bot.py
    -- change on line 5 in get_data.py
    -- change on line 29 in update.py

-----------------------------------------------------------------------------
 bot.py
 
 This program reply to the user who interact with bot.
 
 Program reply is based of command enter by telegram user
 
 this program runs till we stop it by using ctrl+c
 
 ---------------------------------------------------------------------------
 get_data.py
 
 when first time user interact with bot using /start , user data i.e chat id and user name get store in redis database
 
 is store the data of last command which is /start
 
 user's name and chat id is get store into hash.
 and chat id is get add into set by the program.
 
 --------------------------------------------------------------------------
 update.py
 
 When we execute this program , bot send a message to user by using chat id stored in redis set.
 
 bot sends the message which stored in message_bot.txt
 
 program sending message to user after every 1 min (we can set our value) till we stop the program execution by using ctrl + c
 
 ---------------------------------------------------------------------------------





