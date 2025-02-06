import sqlite3
from chatbot import GroqChatbot

# ANSI color codes
GREEN = "\033[92m"
RESET = "\033[0m"

# Initialize chatbot
chatbot = GroqChatbot()

# Database setup
DATABASE = "scraped_data.db"

def get_latest_scraped_content():
    """Retrieve the most recent scraped content from the database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM scraped_content ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        return row[0] if row else None

def main():
    """Command-line chat loop."""
    print("CLI Chatbot Started. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")  # Get user input
        if user_input.lower() == "exit":
            print("Exiting chatbot.")
            break

        # Check if user is asking about the last scraped website
        keywords = ["what is", "explain", "tell me about", "describe"]
        is_related = any(kw in user_input.lower() for kw in keywords)

        if is_related:
            scraped_content = get_latest_scraped_content()
            if scraped_content:
                full_prompt = f"Context: {scraped_content}\n\nUser: {user_input}"
            else:
                full_prompt = user_input
        else:
            full_prompt = user_input  # Normal chat with no scraped content

        # Generate response from chatbot
        response = chatbot.generate_response(full_prompt)
        
        # Print bot response with green color
        print(f"{GREEN}Bot:{RESET} {response}")

if __name__ == "__main__":
    main()
