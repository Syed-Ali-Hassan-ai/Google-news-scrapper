
# Google News Scraper

This Python script scrapes Google News articles for a specific topic using a pre-defined topic ID. It leverages a modular `GoogleNewsScraper` class for handling the scraping process efficiently.

---

## Features

- **Targeted News Scraping:** Fetches news articles for a specific topic using a hardcoded topic ID.
- **Logging:** Provides informative logging messages to monitor the scraping process.
- **Modular Design:** Uses the `GoogleNewsScraper` class for streamlined functionality and easy extension.

---

## Requirements

### Dependencies

The following Python packages are required:
- `logging` (standard Python library)

Install the custom module and dependencies as needed.

---

## Setup and Usage

1. **Hardcoded Topic ID:**
   - The script currently uses a predefined topic ID:
     ```python
     topic = "CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKUVN5Z0FQAQ"
     ```
   - Replace this with a different topic ID if you want to scrape news for another topic.

2. **Run the Script:**
   Execute the script using Python:
   ```bash
   python main.py
   ```

3. **Output:**
   The scraped news articles are processed and stored as per the implementation in the `GoogleNewsScraper` class.

---

## Code Breakdown

### `scrape_google_news()`
- Initializes the `GoogleNewsScraper` instance.
- Uses a hardcoded topic ID to target specific news.
- Calls the `scrape` method of the `GoogleNewsScraper` class to execute the scraping process.

### Logging
- Uses Python's built-in `logging` module to provide real-time feedback during execution.

### `GoogleNewsScraper` Class
- The actual scraping logic is implemented in the `GoogleNewsScraper` class, which must be defined in the `google_news_scraper.scraper` module.

---

## Customization

### Topic ID
- Replace the `topic` variable with a valid Google News topic ID to scrape news for a different topic.

### Scraper Behavior
- Extend or modify the `GoogleNewsScraper` class in the `google_news_scraper.scraper` module to adjust the scraping behavior.

---

## Future Improvements
- Add support for dynamic input of topic IDs via CLI arguments or environment variables.
- Enhance the scraper to handle multiple topics in a single run.
- Implement error handling for network issues or invalid topic IDs.

---

## License

This project is released under the MIT License. Feel free to use, modify, and distribute the code.

---

## Credits

Developed using:
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [Google News](https://news.google.com/)

