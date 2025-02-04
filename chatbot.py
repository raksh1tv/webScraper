import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GroqChatbot:
    def __init__(self, api_key=None):
        """
        Initialize the Groq API client.

        Args:
            api_key (str): Your Groq API key.
        """
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/v1/chat"

    def generate_response(self, message, max_tokens=150, temperature=0.7):
        """
        Generate a response from the Groq API.

        Args:
            message (str): The user's input message.
            max_tokens (int): The max number of tokens in the response.
            temperature (float): Controls response creativity.

        Returns:
            str: Chatbot response.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": [{"role": "user", "content": message}],
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            response_data = response.json()
            return response_data['choices'][0]['message']['content']
        
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
