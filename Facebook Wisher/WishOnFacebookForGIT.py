import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.facebook.com")

userid='YOUR USER ID'
passwordToIt='YOUR PASSWORD'

driver.find_element_by_xpath('//*[@id="email"]').send_keys(userid)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(passwordToIt)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
driver.get('https://www.facebook.com/events/birthdays/')
birthdayDiv = driver.find_element_by_xpath('//*[@id="birthdays_content"]/div[1]/div[2]')
totalBirthdaysCollection = birthdayDiv.find_elements_by_class_name('_tzm')

for eachBirthday in totalBirthdaysCollection:
    name = eachBirthday.find_element_by_class_name('_tzn').text
    divId = eachBirthday.find_element_by_tag_name('textarea').get_attribute('id')
    eachBirthday.find_element_by_xpath('//*[@id="'+str(divId)+'"]').send_keys('Happy Birthday ' + str(name).split()[0] + ' !!!!' )
    eachBirthday.find_element_by_xpath('//*[@id="'+str(divId)+'"]').send_keys(Keys.ENTER)

time.sleep(4)
driver.close()
print("Wished Everyone Happy Birhtday !!!")