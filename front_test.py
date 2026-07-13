import requests
import json

while True:
    front = input("Front: ")
    if front == "-1":
        break
    back = input("Back: ")
    deck = input("Deck: ")

    word_audio = {"word":front}

    payload = {
        "front":front,
        "back":back,
        "deck":deck
    }

    request_audio = requests.post("http://localhost:5000/audio", json=word_audio)

    print(request_audio.json())

    request_create = requests.post("http://localhost:5000/create", json=payload)

    print(request_create.json())
