from flask import Blueprint
import requests

save_card = Blueprint("save_card",__name__)


@save_card.route("/create/front/<front>/back/<back>/deck/<deck>", methods=["POST"])
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
        return f"card created! -----> {response}"
    except Exception as e:
        return f"Error at: {e}"



