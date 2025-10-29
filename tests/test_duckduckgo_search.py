import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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

@pytest.fixture
def go_to_page(driver):
    driver.get("https://duckduckgo.com")



def test_search(driver, go_to_page):
    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.send_keys("Playwright", Keys.ENTER)
    results = driver.find_elements(By.CSS_SELECTOR, "article")
    assert len(results) > 0
    time.sleep(2)