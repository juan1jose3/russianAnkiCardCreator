from flask import Blueprint, request, jsonify

edit_endpoint = Blueprint("edit_endpoint", __name__)


# I have to modify this endpoint
@edit_endpoint.route("edit_card/<int:card_id>", methods=["PUT"])
def edit_card(card_id):
    try:
        front = request.form["front_card"]
        back = request.form["back_card"]
        deck = request.form["deck_card"]
        return jsonify({"Card edited": "success"})
    except Exception as e:
        return jsonify({"error":e})

    
