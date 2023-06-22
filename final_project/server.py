from machinetranslation.translator import english_to_french, french_to_english
from deep_translator import MyMemoryTranslator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french(textToTranslate)
    return f"Translated text to French: {translated_text}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = french_to_english(textToTranslate)
    return f"Translated text to English: {translated_text}"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
