# Traducteur grace au modèle groq, PyQt5 & LangChain Project

Ce projet est un chatbot développé en Python qui utilise les bibliothèques LangChain et Groq.

## Fonctionnalités

* Interface graphique PyQt5
* Logique du chatbot intégrée avec LangChain et Groq
* Prompt & formtage  dédier a la correction de texte dans différents langues

* Sélection de 10 langues différentes & intententions différentes
* Export des échanges sous format dans chat_log.csv


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
│   ├── config.py                # Configuration des variables d'environnement et des constantes
│   ├── gui.py                   # Interface graphique PyQt5
│   ├── chatbot.py               # Logique du chatbot (intégration avec LangChain et Groq)
│
│
├── requirements.txt             # Liste des dépendances Python
├── README.md                    # Documentation du projet
└── main.py                      # Script pour démarrer l'application

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

## Impact des LLm sur perfermance ( ~Avis de claude )

1. Llama 3.1 70b Versatile : 9/10
   - Excellente qualité de traduction
   - Bonne vitesse pour sa taille
   - Polyvalence pour gérer différents aspects de votre tâche

2. Mixtral 8x7b 32768 : 8.5/10
   - Très bonnes performances générales
   - Bon équilibre entre qualité et efficacité
   - Potentiellement plus rapide que le 70b

3. Llama 3.1 405b Reasoning : 8/10
   - Qualité de traduction probablement supérieure
   - Potentiellement plus lent et gourmand en ressources
   - Peut-être surdimensionné pour la tâche

4. Gemma2 9b It : 7.5/10
   - Bon compromis entre performance et efficacité
   - Probablement plus rapide que les plus grands modèles
   - Qualité potentiellement inférieure aux modèles plus grands

5. Llama 3.1 8b Instant : 7/10
   - Très rapide
   - Efficace en termes de ressources
   - Qualité probablement inférieure aux modèles plus grands

6. Llama3 70b 8192 : 8.5/10
   - Similaire au Llama 3.1 70b Versatile
   - Potentiellement optimisé différemment

7. Gemma 7b It : 7/10
   - Rapide et efficace
   - Qualité probablement inférieure aux modèles plus grands

8. Llama3 8b 8192 : 6.5/10
   - Très rapide et efficace
   - Qualité probablement inférieure aux modèles plus grands

9. Llama3 Groq 70b 8192 Tool Use Preview : 8.5/10
   - Potentiellement très performant pour des tâches complexes
   - L'aspect "Tool Use" pourrait ne pas être nécessaire pour la traduction simple

10. Llama3 Groq 8b 8192 Tool Use Preview : 7/10
    - Plus rapide que son homologue 70b
    - Probablement moins performant en qualité de traduction

