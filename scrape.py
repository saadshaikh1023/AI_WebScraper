from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Enter your credentials - the zone name and password
AUTH = "brd-customer-hl_42ca5c58-zone-scrapesense:ylfzy4m4egzg"

SBR_WEBDRIVER = f"https://{AUTH}@zproxy.lum-superproxy.io:9515"


def scrape_website(website):
    print("launching chrome browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)  # use this, or replace with URL of your choice
        print("Taking page screenshot to file page.png")
        driver.get_screenshot_as_file("./page.png")
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    # Below it will checks if it have any scripts or styles then it will remove them by extracting
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    # This get all text and seprate them with a new line
    cleaned_content = soup.get_text(separator="\n")
    # Somethime we have unncearry \n in out html code that we remove by belowe code
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content

# This fucn helps us to send the text in batches so that the gpt can take it as theres a limit of 8k char for safe side we take 6k
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
