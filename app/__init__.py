from flask import Flask


def create_app():
    app = Flask(__name__)

    from creator.card_creator.audio_request import acquire_audio
    from creator.card_creator.create_card import save_card
    from creator.card_creator.request_cards import card_info_data
    from views import views 

    app.register_blueprint(acquire_audio)
    app.register_blueprint(save_card)
    app.register_blueprint(card_info_data)
    app.register_blueprint(views)

    return app