from client import client
from config import model, max_tokens

def chat(messages, system=None, temperature=1.0):

    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
        "temperature": temperature
    }

    if system:
        params["system"] = system

    message = ""

    with client.messages.stream(**params)as stream:
        for text in stream.text_stream:
            print(text, end="")
            message = message + text

    return message
