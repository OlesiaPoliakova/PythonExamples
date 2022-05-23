import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope='module', autouse=True)
def browser():
  browser = Chrome(executable_path=ChromeDriverManager().install())
  browser.maximize_window()

  yield browser

  browser.quit()