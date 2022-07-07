from sqlalchemy import true
from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask("Web Translator",template_folder='xzceb-flask_eng_fr/final_project/templates',static_folder='xzceb-flask_eng_fr/final_project/static')
#app.config['EXPLAIN_TEMPLATE_LOADING']=True

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedtext = translator.EnglishToFrench(textToTranslate)


    return translatedtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedtext = translator.FrenchToEnglish(textToTranslate)
    return translatedtext

@app.route("/")
def homepage():
    return render_template("index.html",)
    


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port= '8080', debug=true)
