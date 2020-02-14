from selenium import webdriver
from time import sleep

from credentials import username, password

class TinderBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        #Go to the Tinder Website
        self.driver.get('https://tinder.com')
        #Wait for it to load
        sleep(4)
        #select "Log in with  Facebook" button and click it
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to "Login with Facebook" Window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        #Select the email parameters and enter it
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        #Select the password parameters and enter it
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        
        #Select the login button and click it
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        
        #Switch back to the original Tinder window
        self.driver.switch_to_window(base_window)

        #Handle the intial popups we encounter on logging in
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        """
        Function to select the like button and click on it(Right Swipe)
        """
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        """
        Function to select the dislike button and click on it(Left Swipe)
        """
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        """
        Function to make swipes automatically
        """
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        """
        Function to close the popup 
        """
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()
    
    def close_match(self):
        """
        Function to close the popup once we get a match
        """
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()

