from flask import Blueprint
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os


acquire_audio = Blueprint("make_create",__name__)
load_dotenv()


@acquire_audio.route("/audio/word/<word>", methods=["GET"])
def get_audio(word):

    try:
        anki_media = os.path.expanduser("~/.var/app/net.ankiweb.Anki/data/Anki2/User 1/collection.media/")

        for file in os.listdir(anki_media):
            if f"{word}.mp3" == file:
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
        
        with open(f"{anki_media}{word}.mp3", "wb") as file:
            file.write(audio_bytes)

        

        return "File requested and saved"

    except Exception as e:
        return f"error at: {e}"


