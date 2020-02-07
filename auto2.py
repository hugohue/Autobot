from selenium import webdriver
import time
from keys import usr1, pw1, usr2, pw2

class AutoBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def loginBlackboard(self):
        self.driver.get('https://blackboard.cuhk.edu.hk/')
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="userNameInput"]')
        email.send_keys(usr1)

        pw = self.driver.find_element_by_xpath('//*[@id="passwordInput"]')
        pw.send_keys(pw1)

        btn = self.driver.find_element_by_xpath('//*[@id="submitButton"]')
        btn.click()

    def loginGoogle(self):
        self.driver.get('https://accounts.google.com/ServiceLogin?hl=zh-TW&passive=true&continue=https://www.google.com/search%3Fq%3Dgmail%26oq%3Dgmail%26aqs%3Dchrome..69i57.733j0j7%26sourceid%3Dchrome%26ie%3DUTF-8')
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.send_keys(usr2)

        btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        btn.click()
        time.sleep(2)
        
        pw = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw.send_keys(pw2)

        btn2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        btn2.click()

bot = AutoBot()
bot.loginBlackboard()
bot = AutoBot()
bot.loginGoogle()

'''
while True:       
    bot = AutoBot()
    bot.login()
    time.sleep(10)
'''
