# ScrapeSense AI Web Scraper

ScrapeSense is an AI-powered web scraping tool that allows users to extract specific information from websites based on their custom queries. It combines web scraping techniques with natural language processing to provide intelligent and targeted data extraction.

## Features

- Web scraping using Selenium and BeautifulSoup
- Content parsing with Ollama LLM
- User-friendly interface built with Streamlit
- Customizable queries for targeted information extraction

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Ollama installed with your chosen LLM
- A Bright Data account for proxy services

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/scrapesense.git
   cd scrapesense
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Bright Data:
   - Log in to [Bright Data](https://brightdata.com)
   - Create a new Proxies & Scraping Infrastructure
   - Update the `AUTH` variable in `scrape.py` with your Bright Data username and password

4. Configure Ollama:
   - Ensure Ollama is installed and running
   - Update the `model` variable in `parse.py` with your chosen LLM

## Usage

1. Start the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Enter a website URL in the provided input field.

3. Click "Scrape Site" to fetch the website content.

4. Enter a description of the information you want to extract in the text area.

5. Click "Parse Content" to process the scraped data and retrieve the requested information.

## Project Structure

- `main.py`: The main Streamlit application
- `scrape.py`: Contains functions for web scraping and content cleaning
- `parse.py`: Handles content parsing using the Ollama LLM
- `requirements.txt`: List of Python dependencies
- `chromedriver.exe`: ChromeDriver executable for Selenium

## Contributing

Contributions to ScrapeSense are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Ollama](https://ollama.ai/)
- [Bright Data](https://brightdata.com/)
