import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



url = "https://youtu.be/Vxl5jUltHBo?t=111"
option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)

driver.quit()

