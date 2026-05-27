from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="в понедельник",
    voice_id="hiAckf4ty3e9BrT4e10G",  
    model_id="eleven_v3",
    output_format="mp3_44100_128",
)

play(audio)

