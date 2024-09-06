# Chatbot Multilingue de Correction et Traduction

Ce projet présente un exemple d'intégration d'un chatbot avancé, développé avec les bibliothèques LangChain et Groq. L'application offre des fonctionnalités de correction orthographique, grammaticale, adaptation d'un style, et traduction depuis et vers les langues sélectionnées par l'utilisateur.


## Fonctionnalités

- Interface graphique conviviale développée avec PyQt5
- Choix du modèle dans config.py 
- Logique du chatbot implémentée à l'aide de LangChain et Groq
- Prompts et formatage spécialisés pour la correction de textes dans diverses langues
- Possibilité de sélectionner la langue et l'intention souhaitées
- Exportation des conversations au format CSV (chat_log.csv)


## Dépendances

* Python 3.x
* LangChain
* Groq
* PyQt5

## Installation

1. Cloner le dépôt Git
2. Installer les dépendances avec `pip install -r requirements.txt`
3. Exécuter le chatbot avec `python main.py`

## Architecture


```bash
chatbot_project/
│── main.py                      # Point d'entrée principal de l'application
├── chatbot/
│   ├── config.py                # Prompte, Template de réponse & clefs API
│   ├── gui.py                   # Interface graphique PyQt5
│   ├── chatbot.py               # Logique du chatbot (intégration avec LangChain et Groq)
├── requirements.txt             # Liste des dépendances Python
├── README.md                    # Documentation du projet
└── main.py                      # Script d'entré l'application

```

### Todo
```bash
chatbot_project/
├── tests/                       # TODO
│   ├── __init__.py              # Permet de traiter le dossier comme un package Python
│   ├── test_chatbot.py          # Tests unitaires pour la logique du chatbot
│   ├── test_gui.py              # Tests pour l'interface graphique (si possible avec des mock)│

```
## génération du fichier .exe

```bash
pyinstaller --onefile --windowed --add-data "chatbot;chatbot" --add-data "skin;skin" main.py
```


