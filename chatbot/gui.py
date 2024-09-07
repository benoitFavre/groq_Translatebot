# Importation des modules nécessaires
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QComboBox, QLabel, QProgressBar
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QTextCursor
from threading import Thread
from chatbot.chatbot import ChatbotManager
import time
import csv
from chatbot.config import MODEL_NAME, RESPONSE_TEMPLATE,Languages,Intention_options

class ChatApp(QWidget):
    # Signal pour émettre un nouveau message
    new_message_signal = pyqtSignal(str, str, float)
    start_loading_signal = pyqtSignal()
    stop_loading_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.chatbot_initialized = False
        # Liste des options de langues
        self.options = Languages
        self.intention_options = Intention_options

        # Initialisation des variables pour l'export
        self.last_user_input = ""
        self.last_bot_response = ""
        self.last_response_time = 0
        self.MODEL_NAME = MODEL_NAME

        self.text_zone = QTextEdit(self)
        self.text_zone.setReadOnly(True)
        self.text_zone.setAcceptRichText(True)
        self.initUI()
        self.new_message_signal.connect(self.display_message)
        self.start_loading_signal.connect(self.start_loading)
        self.stop_loading_signal.connect(self.stop_loading)

    def initUI(self):
        # Configuration de l'interface utilisateur
        self.setWindowTitle('Chatbot with PyQt5')
        self.setMinimumSize(QSize(500, 700))

        layout = QVBoxLayout()

        # Création des menus déroulants pour la sélection des langues
        self.var1_label = QLabel("Langue d'origine:")
        self.var1_select = QComboBox(self)
        self.var1_select.addItems([opt[0] for opt in self.options])
        self.var1_select.setCurrentIndex(4)
        layout.addWidget(self.var1_label)
        layout.addWidget(self.var1_select)

        self.var2_label = QLabel("Langue cible:")
        self.var2_select = QComboBox(self)
        self.var2_select.addItems([opt[0] for opt in self.options])
        layout.addWidget(self.var2_label)
        layout.addWidget(self.var2_select)

        # Création du menu déroulant pour la sélection de l'intention cible
        
        self.var3_label = QLabel("Intention cible:")
        self.var3_select = QComboBox(self)
        self.var3_select.addItems([opt[0] for opt in self.intention_options])
        layout.addWidget(self.var3_label)
        layout.addWidget(self.var3_select)

        # Bouton pour initialiser/réinitialiser le ChatbotManager
        self.init_reset_button = QPushButton('Initialiser Chatbot', self)
        self.init_reset_button.clicked.connect(self.toggle_chatbot)
        layout.addWidget(self.init_reset_button)

        # Zone de texte pour afficher les messages
        self.text_zone = QTextEdit(self)
        self.text_zone.setReadOnly(True)
        layout.addWidget(self.text_zone)

        # Champ de saisie pour les messages de l'utilisateur
        self.entry_field = QTextEdit(self)
        self.entry_field.setFixedHeight(150)
        self.entry_field.setAcceptRichText(False)
        layout.addWidget(self.entry_field)

        # Bouton d'envoi
        send_button = QPushButton('Traduire', self)
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        # Bar de progression d'envoi
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setRange(0, 0)  # Indéterminé
        self.loading_bar.setVisible(False)
        layout.addWidget(self.loading_bar)

        # Bouton d'export
        self.export_button = QPushButton('Exporter', self)
        self.export_button.clicked.connect(self.export_to_csv)
        self.export_button.hide()
        layout.addWidget(self.export_button)

        self.setLayout(layout)

    def export_to_csv(self):
        #   print(self.var1_select.currentText())   # origin_language
        #   print(self.var2_select.currentText())   # target_language
        #   print(self.var3_select.currentText())   # intention_options
        #   print(self.last_user_input)             # user_input
        #   print(self.last_bot_response)           # correction,translation,note
        #   print(self.last_response_time)          # response_time 
        #   print(self.last_user_input)             # user_input
        #   print(self.MODEL_NAME)                  # MODEL_NAME
        if isinstance(self.last_bot_response, dict):
            # Récupérer les valeurs des clés 'correction', 'translation' et 'note'
            correction = self.last_bot_response.get('correction', '')
            translation = self.last_bot_response.get('translation', '')
            note = self.last_bot_response.get('note', '')

            # Ouvrir le fichier CSV en mode écriture avec l'encodage UTF-8
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)

                # Écrire les données dans le fichier CSV
                writer.writerow([
                    self.var1_select.currentText(),  # origin_language
                    self.var3_select.currentText(),  # intention_options
                    self.var2_select.currentText(),  # target_language
                    self.last_user_input,  # user_input
                    correction,  # correction
                    translation,  # translation
                    note,  # note
                    self.last_response_time,  # response_time
                    self.MODEL_NAME  # MODEL_NAME
                ])
            self.export_button.hide()

        else:
            print("Erreur : last_bot_response n'est pas un dictionnaire")

    def toggle_chatbot(self):
        # Bascule entre l'initialisation et la réinitialisation du chatbot
        if not self.chatbot_initialized:
            self.initialize_chatbot()
        else:
            self.reset_chat()

    def initialize_chatbot(self):
        self.text_zone.clear()
        # Initialisation du chatbot avec les langues sélectionnées
        var1_name = self.var1_select.currentText()
        var2_name = self.var2_select.currentText()
        var3_name = self.var3_select.currentText()
        var1_value = next(opt[1] for opt in self.options if opt[0] == var1_name)
        var2_value = next(opt[1] for opt in self.options if opt[0] == var2_name)
        var3_value = next(opt[1] for opt in self.intention_options if opt[0] == var3_name)


        if var1_name and var2_name and var1_name != var2_name:
            self.chatbot_manager = ChatbotManager(var1_value, var2_value,var3_value)
            self.chatbot_initialized = True
            self.new_message_signal.emit("Système", f"Chatbot initialisé en **{var1_name}** vers **{var2_name}** avec une intention **{var3_name}**", 0)
            self.init_reset_button.setText('Réinitialiser')
            
            # Remplacement des sélections par des labels
            self.var1_select.setVisible(False)
            self.var2_select.setVisible(False)
            self.var3_select.setVisible(False)
            self.var1_label.setText(f"Langue d'origine: {var1_name}")
            self.var2_label.setText(f"Langue cible: {var2_name}")
            self.var3_label.setText(f"Intention cible: {var3_name}")

        else:
            self.new_message_signal.emit("Système", "Veuillez sélectionner deux langues différentes.", 0)


    def send_message(self):
        if not self.chatbot_initialized:
            self.new_message_signal.emit("Système", "Veuillez d'abord initialiser le chatbot.", 0)
            return

        user_message = self.entry_field.toPlainText().strip()
        if user_message:
            self.new_message_signal.emit("Vous", f"{user_message}", 0)
            self.entry_field.clear()
            self.start_loading_signal.emit()
            Thread(target=self.get_bot_response, args=(user_message,)).start()

    def get_bot_response(self, user_input):
        try:
            start_time = time.time()
            bot_response = self.chatbot_manager.get_response(user_input)
            response= RESPONSE_TEMPLATE.format(**bot_response)
            end_time = time.time()
            response_time = end_time - start_time
            self.new_message_signal.emit("Bot", response, response_time)

            self.last_bot_response = bot_response
            self.last_response_time = response_time
            self.last_user_input = user_input

        except Exception as e:
            self.new_message_signal.emit("Système", f"Une erreur s'est produite: {e}", 0)
            print(e)
        finally:
            self.stop_loading_signal.emit()

    def display_message(self, sender, message, response_time):

        if sender == "Bot"  :
            self.export_button.show()
            formatted_message = f"{message}\n"
            if response_time > 0:
                formatted_message += f"_(Temps de réponse : {response_time:.2f} secondes)_\n"
        else :
            formatted_message = f"**{sender}** :\n{message}\n"

        current_content = self.text_zone.toMarkdown()
        new_content = f"{current_content}\n{formatted_message}"
        self.text_zone.setMarkdown(new_content)
        # Faire défiler vers le bas
        self.text_zone.moveCursor(QTextCursor.End)
        self.text_zone.ensureCursorVisible()

    def start_loading(self):
        self.loading_bar.setVisible(True)

    def stop_loading(self):
        self.loading_bar.setVisible(False)


    def reset_chat(self):
        # Réinitialisation du chat
        self.text_zone.clear()
        self.entry_field.clear()
        self.chatbot_initialized = False
        if hasattr(self, 'chatbot_manager'):
            del self.chatbot_manager
        
        # Réinitialisation des sélections
        self.var1_select.setVisible(True)
        self.var2_select.setVisible(True)
        self.var3_select.setVisible(True)
        self.var1_label.setText("Langue d'origine:")
        self.var2_label.setText("Langue cible:")
        self.var3_label.setText("Intention cible:")

        self.var1_select.clear()
        self.var2_select.clear()
        self.var3_select.clear()
        self.var1_select.addItems([opt[0] for opt in self.options])
        self.var1_select.setCurrentIndex(4)
        self.var2_select.addItems([opt[0] for opt in self.options])
        self.var3_select.addItems([opt[0] for opt in self.intention_options])
        self.init_reset_button.setText('Initialiser Chatbot')
        self.new_message_signal.emit("Système", "Chat réinitialisé. Veuillez sélectionner les langues et l'intention.", 0)