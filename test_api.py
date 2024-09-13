import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_initialize_chatbot():
    url = f"{BASE_URL}/initialize"
    data = {
        "origin_language": "Français",
        "target_language": "Anglais",
        "intention": "Auto"
    }
    response = requests.post(url, json=data)
    print(f"Send Message: {response.status_code} - {response.json()}")    

#def test_send_message():
    url = f"{BASE_URL}/send_message"
    data = {
        "message": "Bonjour, comment allez-vous ?  je suis la premiére interaction web"
    }
    response = requests.post(url, json=data)
    print(f"Send Message: {response.status_code} - {response.json()}")

#def test_export_conversation():
#    url = f"{BASE_URL}/export"
#    response = requests.get(url)
#    print(f"Export Conversation: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    # Tester l'initialisation du chatbot
    test_initialize_chatbot()

