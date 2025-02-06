import requests

class GroqChatbot:
    def __init__(self):
        """
        Initialize the Groq API client with a hardcoded API key.
        """
        self.api_key = "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"  # 🔥 Replace this with your real API key
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"  # ✅ Corrected endpoint

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
            "model": "llama-3.3-70b-versatile",  # ✅ Specify the model
            "messages": [{"role": "user", "content": message}],
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"]
        
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

