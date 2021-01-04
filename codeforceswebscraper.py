from selenium import webdriver
from selenium.common.exceptions import *
import time
from playsound import playsound

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver  = webdriver.Chrome(PATH)
url = 'https://www.codeforces.com/problemset?tags=1200-1400'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]').click()
time.sleep(3)
email = driver.find_element_by_id('handleOrEmail')
email.send_keys('your-username-for-codeforces')
password = driver.find_element_by_id('password')
password.send_keys('your-password-for-codeforces')
driver.find_element_by_id('remember').click()
driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input').click()
time.sleep(6)
count = 0
list = driver.find_elements_by_class_name('accepted-problem')
for i in range(2,100):
    element = driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr['+str(i)+']')
    if element not in list:
        count += 1
        link = driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr['+str(i)+']/td[2]/div[1]/a').get_attribute('href')
        script = "window.open(\'"+link+"\');"
        driver.execute_script(script)
        time.sleep(4)
        if count == 10:
            playsound('insight-578.mp3')
            break
    