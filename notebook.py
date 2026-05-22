from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

client = Anthropic()

model = "claude-sonnet-4-20250514"

max_tokens = 1000

messages = []

def add_user_message(messages,text):
    user_message = {"role":"user","content":text}
    message.append(user_message)

def add_assistant_message(messages,text):
    assistant_message = {"role":"assistant","content":text}
    message.append(assistant_message)

def chat(messages):    

    message = client.messages.create(
        model = model,
        max_tokens = max_tokens,
        messages = message
    )

messages = []


add_user_message(messages, "Define quantum computing in one sentence")

answer = chat(messages)

print[answer]


# print(message.content)
