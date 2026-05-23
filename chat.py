from client import client
from config import model, max_tokens

def chat(messages,system=None):

    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    
    return message.content[0].text
