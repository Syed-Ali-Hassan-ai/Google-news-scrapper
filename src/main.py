"""
    Main module for google_news_scraper.
"""

import logging
from google_news_scraper.scraper import GoogleNewsScraper

# Set up logging
logging.basicConfig(level=logging.INFO)

def scrape_google_news() -> None:
    # Hardcoded topic ID
    topic = "CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKUVN5Z0FQAQ"

    # Initialize the scraper
    scraper = GoogleNewsScraper()

    # Execute the scraping process
    scraper.scrape(topic)

if __name__ == "__main__":
    scrape_google_news()
