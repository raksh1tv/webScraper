import os
import sqlite3
from flask import Flask, render_template, request, jsonify
from scraper import scrape_website
from chatbot import GroqChatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# Initialize Chatbot
chatbot = GroqChatbot(api_key=groq_api_key)

# Database setup
DATABASE = "scraped_data.db"

def init_db():
    """Initialize the database and create table if not exists."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scraped_content (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                content TEXT
            )
        """)
        conn.commit()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """Handle the web scraping request and store/retrieve content."""
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Check if data already exists
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM scraped_content WHERE url = ?", (url,))
        row = cursor.fetchone()
        if row:
            return jsonify({'content': row[0], 'cached': True})  # Return cached data

    # Scrape the website
    scraped_data = scrape_website(url)
    if 'error' in scraped_data:
        return jsonify(scraped_data), 400

    # Store in database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scraped_content (url, content) VALUES (?, ?)", (url, scraped_data['text']))
        conn.commit()

    return jsonify({'content': scraped_data['text'], 'cached': False})

@app.route('/chat', methods=['POST'])
def chat():
    """Handle the chatbot request."""
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
