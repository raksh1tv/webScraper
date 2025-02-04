import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrape a website and extract text and links.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing the scraped text and links.
    """
    try:
        # Ensure the URL includes a schema (http:// or https://)
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url  # Default to https if no schema is provided

        # Fetch the website content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data (e.g., text and links)
        data = {
            'text': soup.get_text(separator=' ', strip=True),  # Extract all text
            'links': [a['href'] for a in soup.find_all('a', href=True)]  # Extract all links
        }
        return data
    except Exception as e:
        return {'error': str(e)}