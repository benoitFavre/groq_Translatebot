from chatbot.groq_credential import GROQ_API_KEY_PERSO

# Définition des variables utiles au projets

# DClefs de l'api

GROQ_API_KEY = GROQ_API_KEY_PERSO

MODEL_NAME = 'llama-3.1-70b-versatile'
# MODEL_NAME = 'mixtral-8x7b-32768'
# MODEL_NAME = 'gemma2-9b-it'

def SYSTEM_PROMPT(origin_language,intention_options, target_language):

    return f"""
    Your first task is to understand the text and correct it in {origin_language} {intention_options}.
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


Languages = [
    ("Anglais", "English"),
    ("Chinois", "Chinese"),
    ("Espagnol", "Spanish"),
    ("Arabe", "Arabic"),
    ("Français", "French"),
    ("Russe", "French Gangsta rap"), 
    ("Allemand", "German"),
    ("Portugais", "Portuguese"),
    ("Hindi", "Hindi"),
    ("Japonais", "Japanese")
]

Intention_options = [
    ("Auto", ""),
    ("Bavard", "in a more chatty way"),
    ("Enjoué", "in a more cheerful way"),
    ("Sérieux", "in a more serious way"),
    ("Timide", "in a more shy way"),
    ("Réfléchi", "in a more thoughtful way"),
    ("Optimiste", "in a more optimistic way"),
    ("Pessimiste", "in a more pessimistic way"),
    ("Indécis", "in a more indecisive way"),
    ("Décisif", "in a more decisive way"),
    ("Émotif", "in a more emotional way")
]

Intention_options = [
    ("Auto", ""),
    ("Bavard", "in a completely more chatty way"),
    ("Comique", "in a hilariously over-the-top way"),
    ("Surréaliste", "in a completely surreal, dreamlike way"),
    ("Drastique", "in an unapologetically drastic way"),
    ("Dramatique", "as if narrating the climax of a tragic opera"),
    ("Insolent", "with a touch of irreverent sass"),
    ("Paranoïaque", "as if expecting a conspiracy behind every word"),
    ("Cynique", "with a healthy dose of sarcasm and cynicism"),
    ("Philosophique", "as if pondering the meaning of life"),
    ("Excentrique", "with wild, quirky, and eccentric flair"),
    ("Exagéré", "as if everything is the biggest deal ever"),
    ("Flamboyant", "in an overly flamboyant and colorful way"),
    ("Mystique", "with a cryptic, otherworldly aura"),
    ("Hyperactif", "as if powered by an infinite caffeine rush"),
    ("Stupéfait", "as if every word is a mind-blowing revelation"),
    ("Autoritaire", "in a commanding, authoritative tone"),
    ("Maternel/Paternel", "with a protective, nurturing tone"),
    ("Provocateur", "in a deliberately provocative manner"),
    ("Mystérieux", "in a subtly enigmatic and cryptic way")

]

#Intention_options = [
#    ("Auto", ""),
#    ("Chaleureux", "in a warm and welcoming way"),
#    ("Autoritaire", "in a commanding, authoritative tone"),
#    ("Empathique", "with deep empathy and understanding"),
#    ("Sarcastique", "in a biting, sarcastic manner"),
#    ("Encourageant", "in a highly motivating and supportive way"),
#    ("Solennel", "in a solemn and formal tone"),
#    ("Colérique", "with barely contained rage"),
#    ("Ironique", "with a heavy dose of irony"),
#    ("Décontracté", "in a super chill, laid-back style"),
#    ("Pragmatique", "with a down-to-earth, practical approach"),
#    ("Maternel/Paternel", "with a protective, nurturing tone"),
#    ("Provocateur", "in a deliberately provocative manner"),
#    ("Mystérieux", "in a subtly enigmatic and cryptic way"),
#    ("Inspirant", "in an uplifting, inspirational style"),
#    ("Sévère", "with an unforgiving, strict attitude")
#]