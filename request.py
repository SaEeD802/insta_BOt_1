from selenium import webdriver
from info import user, passwd
from time import sleep

class Bot():
    def __init__(self):
        self.login(user, passwd)

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        username_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(2)
        password_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
        sleep(5)
        self.driver.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(3)

        number_of_clicks = 0
        while number_of_clicks < 1: # عددش رو خودت باید تعیین کنی و حتما باید درست باشه
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/main/button').click()
            sleep(2)
            number_of_clicks += 1
        #  اگر درخواست رکوئست کمتر از حد بود میشه این تیکه کد رو کامنت کرد
        
        list_of_usernames = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_usernames.append(names.text)

        for i in list_of_usernames:
            self.driver.get(f"https://www.instagram.com/{i}")
            sleep(2)
            # Requested
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button/div').click()
            # باید ببینی اکس پث آن چیست ممکن است متفاوت باشه
            sleep(1)
            # UnFollow
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]').click()
            # باید ببینی اکس پث آن چیست ممکن است متفاوت باشه
            
def main():
    myBot = Bot()

if __name__ == '__main__':
    main()