from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
import time
import getpass
from playsound import playsound

def check(driver, script):
    driver.execute_script(script)
    #print('Page Loading')
    time.sleep(6)
    #print('Page Loaded')
    driver.switch_to.window(driver.window_handles[-1])
    prev_likes = int(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]/span').get_attribute('innerHTML'))
    dislikes = int(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[2]/span').get_attribute('innerHTML'))
    if (prev_likes/(dislikes+prev_likes))*100 > 65:
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]').click()
        likes = int(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]/span').get_attribute('innerHTML'))
        if likes < prev_likes:
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/button[1]').click()
        return True
    else:
        return False

#em = input('Enter Email: ')
#pa = getpass.getpass(prompt="Enter password: ")

em = 'your-email-for-leetcode'
pa = 'your-password-for-leetcode'

PATH = 'C:\Program Files (x86)\chromedriver.exe'

count = 0

driver = webdriver.Chrome(PATH)
driver.get('https://leetcode.com/problemset/all/?status=Todo&difficulty=Medium')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/thead/tr/th[5]').click()
driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/thead/tr/th[5]').click()
driver.find_element_by_xpath('//*[@id="navbar-right-container"]/div[4]/a[2]').click()
email = driver.find_element_by_xpath('//*[@id="id_login"]')
email.send_keys(em)
password = driver.find_element_by_xpath('//*[@id="id_password"]')
password.send_keys(pa)
driver.find_element_by_id('signin_btn').click()

time.sleep(6)

select = Select(driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span[1]/select'))
select.select_by_visible_text('all')

time.sleep(6)

for i in range(1,100):
    try:
        element = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr['+str(i)+']/td[3]/div/span')
    except NoSuchElementException:
        link = driver.find_element_by_xpath("//*[@id='question-app']/div/div[2]/div[2]/div[2]/table/tbody[1]/tr["+str(i)+"]/td[3]/div/a").get_attribute('href')
        script = "window.open(\'"+link+"\');"
        if check(driver, script)!=True:
            driver.close()
        else:
            count += 1
        driver.switch_to.window(driver.window_handles[0])
        if count == 10:
            driver.switch_to.window(driver.window_handles[1])
            playsound('insight-578.mp3')
            break