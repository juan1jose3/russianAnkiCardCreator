from flask import Blueprint,request,jsonify, render_template
import requests


due_cards = Blueprint("due_cards",__name__)

ANKI_ADDRESS = "http://172.17.0.1:8765"


def get_card_ids():
    try:

        ids = requests.get(
            ANKI_ADDRESS,
            json={
                "action": "findCards",
                "version": 6,
                "params": {
                    "query" : "deck:\"Russian\" is:due"
                }
            }
        )

        return ids.json()["result"]
    except Exception as e:
        return jsonify({"error_fetching": str(e)})


@due_cards.route("/due_cards", methods=["GET"])
def get_due_cards():
    try:
        ids = get_card_ids()

        card_details= requests.get(ANKI_ADDRESS,
            json={
                "action":"cardsInfo",
                "version":6,
                "params":{
                    "cards":[*ids]
                }
            }
        )

        return card_details.json()["result"]

    except Exception as e:
        return jsonify({"error": str(e)})



    