import requests

class GroqChatbot:
    def __init__(self, api_key):
        """
        Initialize the Groq API client.

        Args:
            api_key (str): Your Groq API key.
        """
        self.api_key = api_key
        self.api_url = "https://api.groq.com/v1/chat"  # Ensure this is the correct endpoint

    def generate_response(self, prompt, max_tokens=150, temperature=0.7):
        """
        Generate a response from the Groq API based on the input prompt.

        Args:
            prompt (str): The input prompt for the chatbot.
            max_tokens (int): The maximum number of tokens in the response.
            temperature (float): Controls the creativity of the response (0.0 to 1.0).

        Returns:
            str: The generated response from the Groq API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        try:
            # Send a POST request to the Groq API
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad status codes

            # Parse the response JSON and extract the generated text
            response_data = response.json()
            return response_data['choices'][0]['text']  # Adjust based on Groq API response structure

        except requests.exceptions.RequestException as e:
            # Handle errors (e.g., network issues, invalid API key)
            return f"Error: {str(e)}"