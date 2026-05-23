from config import *
from conversation import add_user_message, add_assistant_message
from chat import chat

messages = []

while True:

    user_input = input("> ")
    print(">",user_input)

    add_user_message(messages, user_input)

    reply = chat(messages)

    add_assistant_message(messages, reply)

    print(reply)


    

