from flask import Flask
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
import requests

app = Flask(__name__)
load_dotenv()

@app.route("/audio/<filename>/word/<word>", methods=["GET"])
def get_audio(filename,word):

    try:
        for file in os.listdir("audioFiles"):
            if filename == file:
                return "File already saved!"
    
        elevenlabs = ElevenLabs(
            api_key=os.getenv("ELEVENLABS_API_KEY"),
        )

        audio = elevenlabs.text_to_speech.convert(
            text=word,
            voice_id="hiAckf4ty3e9BrT4e10G",  
            model_id="eleven_v3",
            output_format="mp3_44100_128",
        )

        audio_bytes = b""
        for chunck in audio:
            audio_bytes += chunck
        
        anki_media = os.path.expanduser("~/.var/app/net.ankiweb.Anki/data/Anki2/User 1/collection.media/")

        with open(f"{anki_media}{filename}", "wb") as file:
            file.write(audio_bytes)

        

        return "File requested and saved"

    except Exception as e:
        return f"error at: {e}"

    
    



@app.route("/create/front/<front>/back/<back>/deck/<deck>", methods=["POST"])
def create_card(front, back, deck):

    try:

        response = requests.post(
            "http://localhost:8765",
            json={
                "action":"addNote",
                "version": 6,
                "params":{
                    "note":{
                        "deckName": f"Russian::{deck}",
                        "modelName": "Basic",
                        "fields":{
                            "Front": f"{front} [sound:{front}.mp3]",
                            "Back": back,
                        },
                        "tags":[
                            "Russian"
                        ]
                    }
                }
            }
        )
        print(response.json())
        return f"card created! -----> {response}"
    except Exception as e:
        return f"Error at: {e}"



def store_audio():
    ...

def connect_to_anki():
    ...




    