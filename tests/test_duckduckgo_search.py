import time
from selenium.webdriver.support import expected_conditions as EC


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_search(driver):
    driver.get("https://duckduckgo.com/?q=Playwright&kl=us-en&ia=web")
    try:
        WebDriverWait(driver, 20).until(lambda d: "playwright" in d.page_source.lower())
    except:
        # Fallback to ultra-light layout if SPA blocks/varies
        driver.get("https://duckduckgo.com/lite/?q=Playwright&kl=us-en")
        WebDriverWait(driver, 20).until(lambda d: "playwright" in d.page_source.lower())

    assert "playwright" in driver.page_source.lower()