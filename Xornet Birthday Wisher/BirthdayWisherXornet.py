from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import win32com.client as win32
import random

chrome_options = Options()
chrome_options.add_argument('-start-maximized')
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

username = 'Your Name'
password = 'Your Password'
wishes = ['Life is too short to be lived counting the years. Just enjoy the ride and make awesome memories...',
          'May your birthday bring you more promotions and perks, more laughs and more smirks. ',
          'Blowing out another candle should mean that you have lived another year with joy and you have made this world a better place. \n Make every day of your life and every candle count.',
          "A birthday is the most special day in one's life. Hope you enjoy it to the fullest. "
          ]


def sendemail(name):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    if outlook.Session.createRecipient(name).Resolve():
        mail.Recipients.Add(name)
        mail.Recipients.ResolveAll()
        mail.Body = 'Happy Birthday, ' + str(name.split(' ')[0]) + ' !!! \n \n' + wishes[
            random.randint(0, len(wishes) - 1)] + '\n \n Have a delightful birthday !!! \n \n - Nishant Modi '
    else:
        mail.Recipients.Add("Nishant Modi")
        mail.Recipients.ResolveAll()
        mail.Body = 'Happy Birthday, ' + str(name) + ' !!! \n \n' + wishes[
            random.randint(0, len(wishes) - 1)] + '\n \n Have a delightful birthday !!! \n \n - Nishant Modi'
    mail.Subject = 'Happy Birthday !!!'
    # mail.HTMLBody = '<h2>HTML Message body</h2>'  # this field is optional
    mail.Send()

    # # To attach a file to the email (optional):
    # attachment = "Path to the attachment"
    # mail.Attachments.Add(attachment)


if __name__ == '__main__':
    driver.get("https://adfs.xoriant.com/adfs/ls/?SAMLRequest=fZHNbsIwEIRfJfI9f24SiAVItByKRFVU0h56qUyyKZYc2"
               "%2FXaFY9fE1oVLpysnd1vtDueIR"
               "%2BkYUvvDuoFvjygi46DVMjGxpx4q5jmKJApPgAy17Ld8mnDaJIxY7XTrZbkArlNcESwTmhFovVqTj4mdF8WeZ937bSu8rprez7Jyq4u"
               "%2B7qidxXlZT%2BtYEIzINEbWAzknASjgCN6WCt0XLkgZfk0zoqYVk1OWVEwWr"
               "%2BTaBWuEYq7kTo4Z5ClKe96TI7aigAmrR5GIZWYkmj5t92DVugHsDuw36KF15fNPx9QBe7KAcVgJJyuTwfdeQmJOZh0rPH80pi3OKod9NxLF6Mh0fY3v3uhOqE%2Bb0e3Pw8he2yabbx93jVkMTt5szEKu7ix4Cy9HDxX15%2B%2B%2BAE%3D&RelayState=https%3A%2F%2Fxornet.xoriant.com%2Fsaml_login")
    driver.find_element_by_xpath('//*[@id="userNameInput"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(Keys.ENTER)

    driver.get("https://xornet.xoriant.com/")
    time.sleep(6)
    BirthdayDiv = driver.find_elements_by_xpath(
        '//*[@id="block-system-main"]/div/div/div/div[1]/div/div[5]/div/div/div/div/div/div/div[1]')

    listOfNames = [BirthdayDiv[0].text]
    checkList = [listOfNames[0].split('\n')]
    birthdate = checkList[0][1]
    while checkList[len(checkList) - 1][1] == checkList[len(checkList) - 1][-1]:
        chk = driver.find_element_by_xpath(
            '//*[@id="block-system-main"]/div/div/div/div[1]/div/div[5]/div/div/div/div/div/div/div[2]/ul/li[3]/a').get_attribute(
            'href')
        driver.get(chk)
        BirthdayDiv = driver.find_elements_by_xpath(
            '//*[@id="block-system-main"]/div/div/div/div[1]/div/div[5]/div/div/div/div/div/div/div[1]')
        listOfNames = [BirthdayDiv[0].text]
        checkList.append(listOfNames[0].split('\n'))
    finalNames = []
    for ele in checkList:
        for x in range(0, len(ele) - 1, 2):
            if ele[x + 1] == birthdate:
                finalNames.append(ele[x])

    driver.close()

    for x in finalNames:
        sendemail(x)
