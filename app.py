import os
import sqlite3
from flask import Flask, render_template, request, jsonify
from scraper import scrape_website
from chatbot import GroqChatbot

# Hardcoded API Key
GROQ_API_KEY = "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"  # Replace with your real API key

app = Flask(__name__)

# Initialize Chatbot
chatbot = GroqChatbot() 


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
    """Render the interactive chat page."""
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

    return jsonify({'message': 'Scraping successful! Data saved in the database.', 'cached': False})


@app.route('/chat', methods=['POST'])
def chat():
    """Handle the chatbot request with scraped content."""
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    # Retrieve the latest scraped content from the database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM scraped_content ORDER BY id DESC LIMIT 1")  # Get the latest content
        row = cursor.fetchone()

    if row:
        scraped_content = row[0]  # Extract text
        full_prompt = f"Context: {scraped_content}\n\nUser: {user_input}"
    else:
        full_prompt = user_input  # No scraped content, just use user input

    # Send combined prompt to chatbot
    response = chatbot.generate_response(full_prompt)

    return jsonify({'response': response})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
