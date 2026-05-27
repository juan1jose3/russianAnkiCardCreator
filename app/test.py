from flask import Flask
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os


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

        with open(f"audioFiles/{filename}", "wb") as file:
            file.write(audio_bytes)

        return "File requested and saved"

    except Exception as e:
        return f"error at: {e}"

    
    



@app.route("/", methods=["POST"])
def create_card():
    return "card created!"


def store_audio():
    ...

def connect_to_anki():
    ...




    