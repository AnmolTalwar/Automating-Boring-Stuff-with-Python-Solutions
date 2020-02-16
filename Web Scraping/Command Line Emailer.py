from selenium import webdriver
import sys

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

elem = browser.find_element_by_css_selector('#identifierId')
elem.send_keys('anmol.talwar93')

elem1 = browser.find_element_by_css_selector('#identifierNext > span')
elem1.click()

elem2 = browser.find_element_by_class_name('Xb9hP')     ##Not Reachable by keyboard Exception, Tried with many things.
elem2.send_keys('Anmol@28111')

elem3 = browser.find_element_by_css_selector('#passwordNext > span')
elem3.click()  

elem4 = browser.find_element_by_css_selector('#\:3n > div > div')
elem4.click()

elem5 = browser.find_element_by_css_selector('#\:9b')
elem5.send_keys(sys.argv[1])

elem6 = browser.find_element_by_css_selector('#\:8t')
elem6.send_keys(sys.argv[2])

elem7 = browser.find_element_by_css_selector('#\:9y')
elem7.send_keys(sys.argv[3])

elem8 = browser.find_element_by_css_selector('#\:8j')
elem8.click()

print("email sent")

browser.quit()





