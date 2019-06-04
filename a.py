import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")

# go to the google home page
driver.get("https://www.zhihu.com/")

# the page is ajaxy so the title is originally this:
print(driver.title)
print(driver.capabilities)
# print(driver.command_executor)
# print(driver.get_network_conditions())
# print(driver.orientation)
# print(driver.window_handles)
# time.sleep(60)
# print(driver.)
# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_partial_link_text("登录")
inputElement.click()
# type in the search
# inputElement.send_keys("cheese!")
# inputElement
# submit the form (although google automatically searches now without submitting)
# inputElement.is_selected()
# inputElement.submit()

try:
    print(1)
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    # print(driver.title)
    # passbbbb

finally:
    driver.quit()