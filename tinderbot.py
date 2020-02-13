from selenium import webdriver
import time
from random import random, randint

class Tinder_Bot():
    def __init__(lowselfesteem):
        lowselfesteem.driver = webdriver.Chrome()

    def login(lowselfesteem):
        lowselfesteem.driver.get('https://tinder.com/')

        lowselfesteem.driver.implicitly_wait(10)

        fb_login = lowselfesteem.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div[2]/button')
        fb_login.click()
        
        base_window = lowselfesteem.driver.window_handles[0]
        pop_up = lowselfesteem.driver.window_handles[1]
        lowselfesteem.driver.switch_to_window(pop_up)

        phone_in = lowselfesteem.driver.find_element_by_xpath('//*[@id="email"]')
        phone_in.send_keys('9197603469')

        pass_in = lowselfesteem.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys('Flutters2013')
        
        fb_login_button = lowselfesteem.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login_button.click()

        lowselfesteem.driver.switch_to_window(base_window)

        location_allow_button = lowselfesteem.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        location_allow_button.click()

        enable_notif = lowselfesteem.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        enable_notif.click()

    def like(lowselfesteem):
        try:
            like_button = lowselfesteem.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
            like_button.click()
        except Exception:
            like_button = lowselfesteem.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
            like_button.click()

    def dislike(lowselfesteem):
        try:
            dislike_button = lowselfesteem.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
            dislike_button.click()
        except Exception:
            dislike_button = lowselfesteem.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]')
            dislike_button.click()

    def close_popups(lowselfesteem):
            try:
                #closes something can't remember.
                pop_up = lowselfesteem.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
                pop_up.click()
            except Exception:
                #closes email alert
                pop_up = lowselfesteem.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
                pop_up.click()
            except Exception:
                #closes matches alert
                pop_up = lowselfesteem.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                pop_up.click()

    def auto_mode(lowselfesteem):
        
        while True:
            time.sleep(4)
            try:
                rand = random()
                if rand < .75:
                    lowselfesteem.like()
                else:
                    lowselfesteem.dislike()
            except Exception:
                lowselfesteem.close_popups()
        
    def match_message(lowselfesteem):
        match_pick = lowselfesteem.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]/a')
        match_pick.click()

        #random pick up line from a list.
        file_object  = open("pickupline.txt", "r")
        pick_up_line = []
        for line in file_object:
            pick_up_line.append(line)

        file_object.close()
        rand = randint(1,119)

        write_message = lowselfesteem.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        write_message.send_keys(pick_up_line[rand])

        time.sleep(1)
        send_message = lowselfesteem.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
        send_message.click()


bot = Tinder_Bot()
bot.login()
