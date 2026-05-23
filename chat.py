from client import client
from config import model, max_tokens

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages
    )
    return message.content[0].text
