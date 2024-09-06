from chatbot.groq_credential import GROQ_API_KEY_PERSO

# Définition des variables utiles au projets
GROQ_API_KEY = GROQ_API_KEY_PERSO

MODEL_NAME = 'llama-3.1-70b-versatile'
# MODEL_NAME = 'mixtral-8x7b-32768'
# MODEL_NAME = 'gemma2-9b-it'

def SYSTEM_PROMPT(origin_language,intention_options, target_language):

    return f"""
    Your first task is to understand the text and correct it in {origin_language} in a more {intention_options} way.
    Translate the corrected text into the current {target_language}.
    finally, include notes in French to help the user understand the translation.
    Make sure not to alter the original message and tone.  
    """


RESPONSE_TEMPLATE = """
**Texte original :** 
>"{correction}"
_________________________
**Traduction :** 
>"{translation}"
_________________________
**Note :**
{note}
_________________________
"""
