'''This file is using methods to make translatin between english and french. '''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''This method translates english inputs into french '''
    if english_text is '':
        return None
    translation = language_translator.translate(text = english_text,model_id= 'en-fr' ).get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''This method translates french inputs into english '''
    if french_text is '':
        return None
    translation = language_translator.translate(text = french_text,model_id= 'fr-en' ).get_result()
    english_text=translation['translations'][0]['translation']
    return english_text

#asd=english_to_french('')
#dse=french_to_english(asd)
#print(asd)
#print(dse)
