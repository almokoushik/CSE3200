from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def account_info():
    with open("acc_info.txt", "r") as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password


email, password = account_info()
tweet = "Hello world! this is mark a ai bot "
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.twitter.com/login")
