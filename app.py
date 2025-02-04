from flask import Flask, render_template, request, jsonify
from scraper import scrape_website
from chatbot import GroqChatbot

app = Flask(__name__)

# Initialize Groq chatbot (replace with your API key)
groq_api_key = "gsk_Xj9pX4AvpOajuMFtBPspWGdyb3FYvUIGyDUNNYdfNrAuX5vFc6eWY"  # Replace with your actual Groq API key
chatbot = GroqChatbot(api_key=groq_api_key)

@app.route('/')
def index():
    """
    Render the main page.
    """
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """
    Handle the web scraping request.
    """
    url = request.json.get('url')
    scraped_data = scrape_website(url)
    return jsonify(scraped_data)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle the chatbot request.
    """
    user_input = request.json.get('message')
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)