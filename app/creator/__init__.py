from flask import Flask


def create_app():
    app = Flask(__name__)

    from .card_creator.audio_request import acquire_audio
    from .card_creator.create_card import save_card

    app.register_blueprint(acquire_audio)
    app.register_blueprint(save_card)

    return app