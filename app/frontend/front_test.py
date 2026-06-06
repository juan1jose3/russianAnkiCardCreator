import requests


front = input("Front: ")
back = input("Back: ")
deck = input("Deck: ")


request_audio = requests.get(f"http://localhost:5000/audio/word/{front}")
print(request_audio)

request_create = requests.post(f"http://localhost:5000/create/front/{front}/back/{back}/deck/{deck}")
print(request_create)
