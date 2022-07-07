import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2022-07-01',authenticator=authenticator)
language_translator.set_service_url(url)

#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages,indent=2))                          code to see if instance is working


def EnglishToFrench(englishtext):
    frenchjson = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    # print(json.dumps(frenchjson, indent=2, ensure_ascii=False))
    # code to see if translation is working
    for i in frenchjson['translations']:
        frenchtext = i['translation']

    # print(frenchtext)  code to see if translation is working
    return frenchtext

# EnglishToFrench("Hi how are you")

def FrenchToEnglish(frenchtext):
    englishjson = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    for i in englishjson['translations']:
        englishtext = i['translation']
      #  print(englishtext)    code to seee if translation is working
        return englishtext

#FrenchToEnglish("Salut comment tu es")
