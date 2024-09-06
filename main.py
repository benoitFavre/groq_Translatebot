import sys
from PyQt5.QtWidgets import QApplication
from chatbot.gui import ChatApp
from skin.styles import dark_style

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(dark_style)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
