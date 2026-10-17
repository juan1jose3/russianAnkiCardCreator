from flask import Blueprint,request,jsonify, render_template
import requests


due_cards = Blueprint("due_cards",__name__)

ANKI_ADDRESS = "http://172.17.0.1:8765"


def query_anki(action, params=None):
    payload = {"action":action, "version":6}

    if params:
        payload["params"] = params

    response = requests.post(ANKI_ADDRESS, json=payload, timeout=5)
    data = response.json()

    if data.get("error"):
        raise RuntimeError(data["error"])  
    return data.get("result", []) 



@due_cards.route("/due_cards", methods=["GET"])
def get_due_cards():
    try:
        ids = query_anki("findCards", {"query": 'deck:"Russian" is:due'})

        if not ids:
            return jsonify([])

        card_details = query_anki("cardsInfo", {"cards": ids})
        return card_details

    except Exception as e:
        return jsonify({"error": str(e)}), 500



    