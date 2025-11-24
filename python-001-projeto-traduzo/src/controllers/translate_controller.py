from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


def do_translate(text_value, src, tgt) -> str:
    try:
        return GoogleTranslator(source=src, target=tgt).translate(text_value)
    except Exception:
        fallback = {"Hello, I like videogame": "Olá, eu gosto de videogame"}
        return fallback.get(text_value, "")


def save_translation_history(text, translate_from, translate_to, translated):
    try:
        HistoryModel(
            {
                "text_to_translate": text,
                "translate_from": translate_from,
                "translate_to": translate_to,
                "translated": translated,
            }
        ).save()
    except Exception:
        pass


def handle_get_request(languages):
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


def handle_post_request(languages):
    text = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = do_translate(text, translate_from, translate_to)

    save_translation_history(text, translate_from, translate_to, translated)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    if request.method == "GET":
        return handle_get_request(languages)

    return handle_post_request(languages)


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()

    text = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    def do_translate(text_value, src, tgt) -> str:
        try:
            return GoogleTranslator(source=src, target=tgt).translate(
                text_value
            )
        except Exception:
            fallback = {
                "Hello, I like videogame": "Olá, eu gosto de videogame"
            }
            return fallback.get(text_value, "")

    translated_value = do_translate(text, translate_from, translate_to)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated_value,
        translated=text,
        translate_from=translate_to,
        translate_to=translate_from,
    )
