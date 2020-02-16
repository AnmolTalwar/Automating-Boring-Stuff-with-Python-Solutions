from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://play2048.co/')

html = browser.find_element_by_tag_name('html')

browser.execute_script("window.scrollTo(0, 200)") 

while True:
    html.send_keys(Keys.UP)
    time.sleep(1)
    html.send_keys(Keys.RIGHT)
    time.sleep(1)
    html.send_keys(Keys.DOWN)
    time.sleep(1)
    html.send_keys(Keys.LEFT)
    time.sleep(1)

    try:
        elem = browser.find_element_by_css('.retry-button')
        elem.click()
        continue
    except:
        #print("Still Playing")
        continue
    



