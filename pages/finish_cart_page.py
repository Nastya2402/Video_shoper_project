import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base



class Finish_cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    finish_cart = "//*[@id='basket_block']/div[3]/div/button"
    name_product = "//*[@id='basket_block']/div[1]/div[1]/div/div[2]/div[2]"
    price_product = "//*[@id='basket_block']/div[1]/div[2]/div[2]/div[1]/span"

    finish_cart_2 = "//*[@id='basket_block']/div[3]/div/button"
    name_product_2 = "//*[@id='basket_block']/div[1]/div[1]/div/div[2]/div[2]"
    price_product_2 = "//*[@id='basket_block']/div[1]/div[2]/div[2]/div[1]/span"


   #Getters

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_finish_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_cart)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_2)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))

    def get_finish_cart_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_cart_2)))
    # Actions


    """Нажимаем оформить заказ"""

    def click_finish_cart(self):
        self.get_finish_cart().click()
        print("Click на оформить заказ")

    """Нажимаем оформить заказ"""

    def click_finish_cart_2(self):
        self.get_finish_cart_2().click()
        print("Click на оформить заказ")


    # Methods
    def finish_product(self):
        self.assert_word(self.get_name_product(), "Samsung Galaxy Z Flip4 F721B 128Gb graphite (графит)")
        self.assert_word(self.get_price_product(), "72 940 ₽")
        time.sleep(10)
        self.click_finish_cart()
    def finish_product_2(self):
        self.assert_word(self.get_name_product_2(), "Samsung Galaxy Z Flip4 F721B 128Gb blue (голубой)")
        self.assert_word(self.get_price_product_2(), "72 940 ₽")
        time.sleep(10)
        self.click_finish_cart_2()