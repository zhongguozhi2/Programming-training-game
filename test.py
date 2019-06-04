import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# options = Options()
browser = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
browser.get("https://www.zhihu.com")

time.sleep(3)
content = browser.find_element_by_xpath("/html/body[@class='EntrySign-body']/div[@id='root']/div/main[@class='App-main']/div[@class='SignFlowHomepage']/div[@class='SignFlowHomepage-content']/div[@class='Card SignContainer-content']/div[@class='SignContainer-inner']/div[@class='SignContainer-switch']/span")
    # 点击login
# login.click()
content.click()
time.sleep(3)

username = browser.find_element_by_xpath(r"/html/body[@class='EntrySign-body']/div[@id='root']/div/main[@class='App-main']/div[@class='SignFlowHomepage']/div[@class='SignFlowHomepage-content']/div[@class='Card SignContainer-content']/div[@class='SignContainer-inner']/div[@class='Login-content']/form[@class='SignFlow']/div[@class='SignFlow-account']/div[@class='SignFlowInput SignFlow-accountInputContainer']/div[@class='SignFlow-accountInput Input-wrapper']/input[@class='Input']")
username.send_keys("18239443172")
password = browser.find_element_by_xpath(r"//input[@name='password']")

password.send_keys("huang19970609")
submit = browser.find_element_by_xpath(r"/html/body[@class='EntrySign-body']/div[@id='root']/div/main[@class='App-main']/div[@class='SignFlowHomepage']/div[@class='SignFlowHomepage-content']/div[@class='Card SignContainer-content']/div[@class='SignContainer-inner']/div[@class='Login-content']/form[@class='SignFlow']/button[@class='Button SignFlow-submitButton Button--primary Button--blue']")
submit.click()


# 滚动到页面底部
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")