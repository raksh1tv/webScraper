Web Scraper, Chatbot, and CLI Agent

Overview

This project is a web application that integrates a web scraper, a chatbot, and a CLI agent. Users can input a URL to scrape website content, which is stored in a SQLite database. The chatbot can then use this scraped data to provide context-aware responses. Additionally, a CLI agent allows users to interact with the chatbot via the command line.

**Features

Scrapes website content and stores it in a database.

Caches previously scraped content to avoid redundant requests.

Chatbot retrieves and uses the latest scraped content for responses.

Interactive web UI for user interaction.

CLI agent for command-line interaction.

Dark theme styling for a modern look.

**Project Structure

project_root/
│-- static/
│   ├── styles.css   # Contains the dark theme and chat UI styles
│-- templates/
│   ├── index.html   # Frontend interface for chat and scraping
│-- app.py           # Flask application handling routes and logic
│-- scraper.py       # Web scraping logic
│-- chatbot.py       # Chatbot integration with Groq API
│-- cli_agent.py     # CLI-based chatbot interaction
│-- scraped_data.db  # SQLite database storing scraped content
│-- README.md        # Project documentation

**Setup Instructions

**Prerequisites

Python 3.8+

Flask

SQLite3

Requests library

**Installation

Clone the repository:

git clone https://github.com/your-repo/webscraper-chatbot.git
cd webscraper-chatbot

Install dependencies:

pip install -r requirements.txt

Set up your API key in app.py and cli_agent.py:

GROQ_API_KEY = "your_actual_api_key_here"


**Run the web application:

python app.py

**Run the CLI agent:

python cli_agent.py  in cmd

**Usage

1 Web App

Open the web app in your browser (http://127.0.0.1:5000).

Enter a URL to scrape.

Ask the chatbot questions related to the scraped content.

2 CLI Agent

Run python cli_agent.py.

Enter a URL to scrape.

Type messages to interact with the chatbot via the command line.

**Clearing the Database

To remove all stored data, run the following command in the SQLite CLI:

sqlite3 scraped_data.db "DELETE FROM scraped_content;"

**Troubleshooting

If you receive a 404 Client Error, verify that the API endpoint is correct.

If the chatbot returns incorrect responses, check if the database contains the correct scraped content.

Use sqlite3 scraped_data.db "SELECT * FROM scraped_content;" to inspect stored data.

Future Improvements

Improve chatbot memory for contextual conversation history.

Support for multiple scraped pages per session.

Deploy the app online with a proper UI.
