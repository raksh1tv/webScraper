import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrape only the provided webpage, extracting its text content.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        dict: Extracted text content, or an error message.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract only text from the page itself, not other linked pages
        page_text = soup.get_text(separator=' ', strip=True)

        return {'text': page_text}
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
