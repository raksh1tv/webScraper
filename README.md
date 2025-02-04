# webScraper
full-stack application that scrapes content from a user-provided website URL. The application should allow users to interact with a chatbot that uses the scraped content to generate responses, leveraging Retrieval-Augmented Generation (RAG) and LLM techniques.

This is a Flask-based web application that allows users to:
✔ Scrape website content (only from the provided URL) and store it for future retrieval.
✔ Chat with an AI-powered chatbot using the Groq API.

🚀 Features
✅ Efficient Web Scraping: Extracts only the text from the given page (ignores external links).
✅ Caching System: Stores scraped content in an SQLite database to prevent redundant requests.
✅ AI Chatbot: Uses Groq's API to generate intelligent responses.
✅ Secure API Key Handling: Uses .env file to store sensitive API keys.
✅ Fast and Lightweight: Built with Flask, BeautifulSoup, and SQLite.

1.Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the root directory and add your Groq API Key:
GROQ_API_KEY=your_groq_api_key_here

 NOTE: YOU CAN USE ANY API YOU WISH TO. API I HAVE USED ACTUALLY ISNT WORKING CORRECTLY SO PLEASE REFER WEB FOR FREE API. EVERYTHING ELSE FROM INSTALLATION TO CODES IS PERFECT!

 How to Run the Application?
 in the terminal type: 
 python app.py
NOTE PLEASE WORK IN A VIRTUAL ENVIRONMENT IT IS RECOMENDED AND ALSO INSTALL ALL THE DEPENDENCIES THERE ONLY

How to start a Virtual envionment? 
venv/scripts/activate

structure: 

├── app.py              # Flask backend
├── scraper.py          # Web scraper (BeautifulSoup)
├── chatbot.py          # Groq Chatbot API integration
├── templates/
│   ├── index.html      # Frontend UI (if needed)
├── static/             # Static files (CSS, JS)
├── .env                # Environment variables (GROQ API Key)
├── README.md           # Project documentation
└── scraped_data.db     # SQLite database (auto-created)

NOTE: API SHOULD NOT BE HARDCODED ALWAYS HIDE THEM USE CREATE AND USE AN .env FILE.
