dark_style = """
QWidget {
    background-color: #2B2B2B;
    color: #E0E0E0;
}

QTextEdit {
    background-color: #353535;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
    padding: 10px;
    font-family: Arial, sans-serif;
    font-size: 16px;
}

QTextEdit:focus {
    border: 1px solid #3E3E3E;
}

QPushButton {
    background-color: #4A4A4A;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
    padding: 5px;
    font-family: Arial, sans-serif;
    font-size: 16px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #5A5A5A;
}

QPushButton:pressed {
    background-color: #333333;
}

QPushButton:disabled {
    background-color: #555555;
    color: #7A7A7A;
}

QScrollBar:vertical {
    background-color: #2B2B2B;
    width: 12px;
    margin: 22px 0 22px 0;
}

QScrollBar::handle:vertical {
    background-color: #4A4A4A;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #2B2B2B;
    height: 20px;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover {
    background-color: #3E3E3E;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    border: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background-color: #2B2B2B;
}
"""