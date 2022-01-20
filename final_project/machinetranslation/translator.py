"""
This module translates texts from english to french and vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


#create instance of IBM Watson language translator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text = None):
    """
    This function takes the input english text and returns the translated french text
    """
    if (english_text is None):
        return 'Invalid input'
    result = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    translations = result['translations']
    french_text = translations[0]
    return french_text["translation"]


def french_to_english(french_text = None):
    """
    This function takes the input french text and returns the translated english text
    """
    if (french_text is None):
        return 'Invalid input'
    result = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    translations = result['translations']
    english_text = translations[0]
    return english_text["translation"]
