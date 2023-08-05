"""
translator.py: A module for translating text between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.

    Args:
        english_text (str): The text in English to be translated.

    Returns:
        str: The translated text in French.
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English.

    Args:
        french_text (str): The text in French to be translated.

    Returns:
        str: The translated text in English.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
