import unittest
from chatbot.chatbotservice import ChatbotService
from chatbot.config import RESPONSE_TEMPLATE, Languages, Intention_options

class TestChatbotService(unittest.TestCase):
    def setUp(self):
        self.chatbot_service = ChatbotService(Languages, Intention_options, RESPONSE_TEMPLATE)

    def test_initialize_chatbot(self):
        var1_name = "Français"
        var2_name = "Anglais"
        var3_name = "Traduction"
        message = self.chatbot_service.initialize_chatbot(var1_name, var2_name, var3_name)
        self.assertIsNotNone(message)

    def test_send_message(self):
        var1_name = "Français"
        var2_name = "Anglais"
        var3_name = "Bavard"
        self.chatbot_service.initialize_chatbot(var1_name, var2_name, var3_name)
        user_message = "Bonjour, comment allez-vous ? prét pour les course ?"
        response = self.chatbot_service.send_message(user_message)
        self.assertIsNotNone(response)
    
    def test_send_message(self):
        var1_name = "Français"
        var2_name = "Anglais"
        var3_name = "Surréaliste"
        self.chatbot_service.initialize_chatbot(var1_name, var2_name, var3_name)
        user_message = "Bonjour, comment allez-vous ? prét pour les course ?"
        response = self.chatbot_service.send_message(user_message)
        self.assertIsNotNone(response)

    def test_send_message(self):
        var1_name = "Français"
        var2_name = "Anglais"
        var3_name = "Comique"
        self.chatbot_service.initialize_chatbot(var1_name, var2_name, var3_name)
        user_message = "Bonjour, comment allez-vous ? prét pour les course ?"
        response = self.chatbot_service.send_message(user_message)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
