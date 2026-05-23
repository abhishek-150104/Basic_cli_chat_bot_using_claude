from config import *
from conversation import add_user_message, add_assistant_message
from chat import chat

messages = []

while True:

    user_input = input("> ")
    print(">",user_input)

    # system = input("> ")

    system = """
    You are a patient math tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step
    """

    add_user_message(messages, user_input)

    reply = chat(messages, temperature=1.0)

    add_assistant_message(messages, reply)

    print(reply)


    

