from flask import Blueprint,request,jsonify, render_template
import requests

card_info_data = Blueprint("due_cards",__name__)

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




@card_info_data.route("/due_cards", methods=["GET"])
def get_due_cards():
    try:
        status = request.args.get("status")

        status_queries = {
            "due": 'deck:"Russian" is:due',
            "new": 'deck:"Russian" is:new',
            "all":'deck:"Russian"'
        }

        if status not in status_queries:
            return jsonify({"error": f"Invalid status '{status}'. Choose from 'due', 'new', or 'all'."}), 400

        query_string = status_queries[status]


        ids = query_anki("findCards", {"query": query_string})
        if not ids:
            return jsonify([])

        card_details = query_anki("cardsInfo", {"cards": ids})
        return card_details

    except Exception as e:
        return jsonify({"error": str(e)}), 500



    