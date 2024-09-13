from flask import Flask, request, jsonify
from chatbot.chatbotservice import ChatbotService
from chatbot.config import RESPONSE_TEMPLATE, Languages, Intention_options

app = Flask(__name__)

# Initialiser le service chatbot (on peut aussi le faire au moment de l'initialisation)
chatbot_service = ChatbotService(Languages, Intention_options, RESPONSE_TEMPLATE)
@app.route('/initialize', methods=['POST'])
def initialize_chatbot():
    data = request.json
    origin_lang = data.get('origin_language')
    target_lang = data.get('target_language')
    intention = data.get('intention')

    # Initialiser le chatbot avec les paramètres fournis
    response_message = chatbot_service.initialize_chatbot(origin_lang, target_lang, intention)
    
    return jsonify({"message": response_message})

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message')

    # Vérifier si le chatbot est initialisé
    if not chatbot_service.chatbot_manager:
        return jsonify({"error": "Chatbot non initialisé."})

    # Envoyer le message à la méthode send_message du service
    bot_response = chatbot_service.send_message(user_message)
    return jsonify({"response": bot_response})

@app.route('/export', methods=['GET'])
def export_conversation():
    # Exporter la conversation sous forme de CSV
    chatbot_service.export_to_csv()
    return jsonify({"message": "Conversation exportée avec succès."})

if __name__ == '__main__':
    app.run(debug=True)
