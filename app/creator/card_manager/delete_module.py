from flask import Blueprint, request, jsonify
from creator.card_creator.request_cards import query_anki

delete_endpoint = Blueprint("delete_endpoint",__name__)

@delete_endpoint.route("/delete_card/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    try:
        response_ans = query_anki("deleteNotes", {"notes":[card_id]})
        return jsonify({"cardEliminated": response_ans})
    except Exception as e:
        return jsonify({"error": e}), 500




