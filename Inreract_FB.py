from argparse import Action
from random import randint
import time
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import random, string

from base import TIMEOUT, BasePage

#tương tác faceboook

class INRERACT_F(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        # Khai báo các phần tử trên trang đăng nhập
        self.LIKE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#actions_964927471524208 > table > tbody > tr > td:nth-child(1) > a")
        self.COMMENT_INPUT_LOCATOR = (By.NAME,"comment_text")
        self.COMMENT_BUTTON_LOCATOR = (By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[3]/form[1]/table/tbody/tr/td[2]/div/input")
        self.INBOX_INPUT_LOCATOR = (By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/table/tbody/tr/td[1]/textarea")
        self.INBOX_BUTTON_LOCATOR = (By.NAME,"send")
    
    
    def LIKE(self, Uid):
        self.open(f'/{Uid}')
        time.sleep(3)
        self.click(self.LIKE_BUTTON_LOCATOR)
    

    def COMMENT(self,Uid,Content):
        self.open(f'/{Uid}')
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(self.COMMENT_INPUT_LOCATOR)
        )
        self.click(self.COMMENT_INPUT_LOCATOR)
        for i in range(randint(1,3)):
            self.send_keys(self.COMMENT_INPUT_LOCATOR,INRERACT_F.randomWord(length=10))
            self.clear_keys(self.COMMENT_INPUT_LOCATOR)
        self.send_keys(self.COMMENT_INPUT_LOCATOR,Content)
        self.press_enter_key()
        #self.click(self.COMMENT_BUTTON_LOCATOR)
    

    def INBOX(self,Uid_Acc,Content):
        self.base_url = "https://mbasic.facebook.com/messages/read/?fbid="
        self.open(f'{Uid_Acc}')
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(self.INBOX_INPUT_LOCATOR)
        )
        self.move_to_element(self.INBOX_INPUT_LOCATOR)
        self.click(self.INBOX_INPUT_LOCATOR)
        self.send_keys(self.INBOX_INPUT_LOCATOR,Content)
        self.click(self.INBOX_BUTTON_LOCATOR)


    def randomWord(length=10):
        consonants="bcdfghjklmnpqrstvwxyz"
        vowels="aeiou"
        return "".join(random.choice((consonants,vowels)[i%2]) for i in range(length))


    def test(self):
        self.open()
        self.click((By.ID,"m_login_email"))
        self.send_keys((By.ID,"m_login_email"),INRERACT_F.randomWord(length=10))
        self.clear_keys((By.ID,"m_login_email"))


driver = webdriver.Chrome()
INRERACT_FB = INRERACT_F(driver, 'https://mbasic.facebook.com')
INRERACT_FB.LIKE("964926491524306")
time.sleep(5)
INRERACT_FB.COMMENT("964926491524306","test Comment")
time.sleep(5)
INRERACT_FB.INBOX("100000631981875","test INBOX")
time.sleep(3)

