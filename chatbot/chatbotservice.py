from chatbot.chatbot import ChatbotManager
import csv
import time

class ChatbotService:
    def __init__(self, options, intention_options, RESPONSE_TEMPLATE):
        self.options = options
        self.intention_options = intention_options
        self.RESPONSE_TEMPLATE = RESPONSE_TEMPLATE
        self.chatbot_manager = None
        self.last_response = {}
        self.last_response_time = 0
        self.last_user_input = ""
        self.seleted_origin_language= ""
        self.seleted_target_language= ""
        self.seleted_intention_options= ""

    def initialize_chatbot(self, var1_name, var2_name, var3_name):
        self.seleted_origin_language= var1_name
        self.seleted_target_language= var2_name
        self.seleted_intention_options= var3_name
        var1_value = next(opt[1] for opt in self.options if opt[0] == var1_name)
        var2_value = next(opt[1] for opt in self.options if opt[0] == var2_name)
        var3_value = next(opt[1] for opt in self.intention_options if opt[0] == var3_name)
        self.chatbot_manager = ChatbotManager(var1_value, var2_value, var3_value)
        return f"Je suis paramétré pour corriger en  **{var1_name}** et apporter une traduction en **{var2_name}** dans une humeur **{var3_name}**"
    
    def send_message(self, user_message):
        if not self.chatbot_manager:
            return "Veuillez d'abord initialiser le chatbot."
        
        start_time = time.time()
        bot_response = self.chatbot_manager.get_response(user_message)
        end_time = time.time()
        response_time = end_time - start_time
        self.last_response = bot_response
        self.last_response_time = response_time
        self.last_user_input = user_message
        response = self.RESPONSE_TEMPLATE.format(**bot_response)

        response += f"_(Temps de réponse : {response_time:.2f} secondes, "
        response += f"Prompt tokens : {self.last_response['token_usage']['prompt_tokens']}, Completion tokens : {self.last_response['token_usage']['completion_tokens']}, Total tokens : {self.last_response['token_usage']['total_tokens']})_"

        return response

    def get_data(self):
        if isinstance(self.last_response, dict) and isinstance(self.last_response['token_usage'], dict):
            try:
                data = {
                    'origin_language': self.seleted_origin_language,
                    'target_language': self.seleted_target_language,
                    'intention_options': self.seleted_intention_options,
                    'user_input': self.last_user_input,
                    'correction': self.last_response.get('correction', ''),
                    'translation': self.last_response.get('translation', ''),
                    'note': self.last_response.get('note', ''),
                    'response_time': self.last_response_time,
                    'model_name': self.last_response.get('model_name', ''),
                    'completion_tokens': self.last_response['token_usage'].get('completion_tokens', ''),
                    'prompt_tokens': self.last_response['token_usage'].get('prompt_tokens', ''),
                    'total_tokens': self.last_response['token_usage'].get('total_tokens', ''),
                    'completion_time': self.last_response['token_usage'].get('completion_time', ''),
                    'prompt_time': self.last_response['token_usage'].get('prompt_time', ''),
                    'queue_time': self.last_response['token_usage'].get('queue_time', '')
                }
                return data
            except KeyError as e:
                raise ValueError(f"Clé manquante : {e}")
        else:
            print("Erreur : last_response n'est pas un dictionnaire")

    def write_to_csv(self, data):
        with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                writer.writerow(list(data.keys()))
            writer.writerow(list(data.values()))

    def export_to_csv(self):
        data = self.get_data()
        self.write_to_csv(data)
