from flask import Blueprint,request,jsonify
from .audio_request import request_text_to_speech
import requests
save_card = Blueprint("save_card",__name__)


@save_card.route("/create", methods=["POST"])
def create_card():

    try:
        front = request.form["front_card"]
        back = request.form["back_card"]
        deck = request.form["deck_card"]

        front = front.replace("?","").replace("!","").replace(",","").replace("/","").replace(":","").replace("*","").strip()

        request_text_to_speech(front)
        response = requests.post(
            "http://172.17.0.1:8765",
            json={
                "action":"addNote",
                "version": 6,
                "params":{
                    "note":{
                        "deckName": f"Russian::{deck}",
                        "modelName": "Basic",
                        "fields":{
                            "Front": f"{front} \n [sound:{front}.mp3]",
                            "Back": back,
                        },
                        "tags":[
                            "Russian"
                        ]
                    }
                }
            }
        )
        return jsonify({"message":"Card created!", "anki_response": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)})



