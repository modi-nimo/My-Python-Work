import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

pathToExtension = "Path To Cyberghost chrome extension"
chrome_options = Options()
chrome_options.add_argument("--load-extension=" + pathToExtension)
chrome_options.add_argument('-start-maximized')

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
screenWidth, screenHeight = pyautogui.size()
currentX, currentY = pyautogui.position()
pyautogui.moveTo(1317, 50)
time.sleep(2)
pyautogui.click()

pyautogui.moveTo(1094, 338)
time.sleep(2)
pyautogui.click()

pyautogui.moveTo(1096, 600)
time.sleep(2)
pyautogui.click()

driver.get("https://www.facebook.com")

userid='username'
passwordToIt='password'

driver.find_element_by_xpath('//*[@id="email"]').send_keys(userid)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(passwordToIt)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
driver.get('https://www.facebook.com/events/birthdays/')
birthdayDiv = driver.find_element_by_xpath('//*[@id="birthdays_content"]/div[1]/div[2]')
totalBirthdaysCollection = birthdayDiv.find_elements_by_class_name('_tzm')

for eachBirthday in totalBirthdaysCollection:
    name = eachBirthday.find_element_by_class_name('_tzn').text
    try:
        divId = eachBirthday.find_element_by_tag_name('textarea').get_attribute('id')
        eachBirthday.find_element_by_xpath('//*[@id="'+str(divId)+'"]').send_keys('Happy Birthday ' + str(name).split()[0] + ' !!!!' )
        time.sleep(1)
        eachBirthday.find_element_by_xpath('//*[@id="'+str(divId)+'"]').send_keys(Keys.ENTER)
    except Exception as e:
        print(name)
time.sleep(4)
driver.close()
print("Wished Everyone Happy Birhtday !!!")