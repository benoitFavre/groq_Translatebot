# Importation des modules nécessaires
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QComboBox, QLabel, QProgressBar
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QTextCursor
from threading import Thread

from chatbot.config import RESPONSE_TEMPLATE, Languages, Intention_options
from chatbot.chatbotservice import ChatbotService

class ChatApp(QWidget):
    # Signal pour émettre un nouveau message
    new_message_signal = pyqtSignal(str, str, float)
    start_loading_signal = pyqtSignal()
    stop_loading_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.chatbot_service = ChatbotService(Languages, Intention_options, RESPONSE_TEMPLATE)
        self.chatbot_initialized = False

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
        self.var1_select.addItems([opt[0] for opt in self.chatbot_service.options])
        self.var1_select.setCurrentIndex(4)
        layout.addWidget(self.var1_label)
        layout.addWidget(self.var1_select)

        self.var2_label = QLabel("Langue cible:")
        self.var2_select = QComboBox(self)
        self.var2_select.addItems([opt[0] for opt in self.chatbot_service.options])
        layout.addWidget(self.var2_label)
        layout.addWidget(self.var2_select)

        # Création du menu déroulant pour la sélection de l'intention cible
        
        self.var3_label = QLabel("Intention cible:")
        self.var3_select = QComboBox(self)
        self.var3_select.addItems([opt[0] for opt in self.chatbot_service.intention_options])
        layout.addWidget(self.var3_label)
        layout.addWidget(self.var3_select)

        self.var1_select.currentTextChanged.connect(self.toggle_param_chatbot)
        self.var2_select.currentTextChanged.connect(self.toggle_param_chatbot)
        self.var3_select.currentTextChanged.connect(self.toggle_param_chatbot)

        
               

        # Zone de texte pour afficher les messages
        self.text_zone = QTextEdit(self)
        self.text_zone.setReadOnly(True)
        layout.addWidget(self.text_zone)

        # Champ de saisie pour les messages de l'utilisateur
        self.entry_field = QTextEdit(self)
        self.entry_field.setFixedHeight(150)
        self.entry_field.setAcceptRichText(False)
        layout.addWidget(self.entry_field)

        
        # Bar de progression d'envoi
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setRange(0, 0)  # Indéterminé
        self.loading_bar.setVisible(False)
        layout.addWidget(self.loading_bar)
        # Bouton d'envoi
        send_button = QPushButton('Traduire', self)
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        # Bouton pour initialiser/réinitialiser le ChatbotManager
        self.init_reset_button = QPushButton('Nettoyer le Chat', self)
        self.init_reset_button.clicked.connect(self.text_zone.clear)
        layout.addWidget(self.init_reset_button)

        # Bouton d'export
        self.export_button = QPushButton('Exporter', self)
        self.export_button.clicked.connect(self.export_to_csv)
        self.export_button.hide()
        layout.addWidget(self.export_button)

        self.setLayout(layout)

    def toggle_param_chatbot(self):
        self.initialize_chatbot()
        # Bascule entre l'initialisation et la réinitialisation du chatbot

    def initialize_chatbot(self):

        # Initialisation du chatbot avec les langues sélectionnées
        var1_name = self.var1_select.currentText()
        var2_name = self.var2_select.currentText()
        var3_name = self.var3_select.currentText()
        message = self.chatbot_service.initialize_chatbot(var1_name, var2_name, var3_name)
        self.new_message_signal.emit("Système", message, 0)
        self.chatbot_initialized = True

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
            response = self.chatbot_service.send_message(user_input)
            self.new_message_signal.emit("Bot", response, 0)
        except Exception as e:
            self.new_message_signal.emit("Système", f"Une erreur s'est produite: {e}", 0)
        finally:
            self.stop_loading_signal.emit()

    def display_message(self, sender, message, response_time):
        if sender == "Bot"  :
            self.export_button.show()
            formatted_message = f"{message}\n"
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
        if(self.chatbot_initialized == True) :
            self.chatbot_initialized = False

    def export_to_csv(self):
        data = self.chatbot_service.get_data()
        self.chatbot_service.write_to_csv(data)
        self.export_button.hide()
