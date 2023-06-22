from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''For english translation'''
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''For french translation'''
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text