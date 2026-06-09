from flask import Blueprint,request,jsonify
import requests
save_card = Blueprint("save_card",__name__)


@save_card.route("/create", methods=["POST"])
def create_card():

    try:
        petition = request.get_json()

        front = petition["front"]
        back = petition["back"]
        deck = petition["deck"]

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
        print(response.json())
        return jsonify({"message":"Card created!", "anki_response": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)})



