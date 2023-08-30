import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base



class Choise_complekt_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    simple = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/label/span"
    revolution = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[4]/div[1]/label/span"
    cart = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[2]/a"
    name_product = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]"
    price_product = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[4]/div[6]/div[3]"

    simple_2 = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/label/span"
    revolution_2 = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[4]/div[1]/label/span"
    cart_2 = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[2]/a"
    name_product_2 = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]"
    price_product_2 = "//*[@id='modalCart']/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[4]/div[6]/div[3]"
   #Getters
    def get_simple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.simple)))


    def get_revolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.revolution)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    def get_simple_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.simple_2)))


    def get_revolution_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.revolution_2)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_2)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))

    def get_cart_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_2)))
    # Actions

    """Убираем комплект простой"""

    def click_simple(self):
        self.get_simple().click()
        print("Click complekt simple")

    """Выбираем комплект револяция"""
    def click_revolution(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.get_revolution().click()
        print("Click complekt revolution")

    """Кликаем на корзину"""
    def click_cart(self):
        self.get_cart().send_keys(Keys.PAGE_DOWN)
        self.get_cart().send_keys(Keys.RETURN)
        print("Click cart")


    """Убираем комплект простой"""

    def click_simple_2(self):
        self.get_simple_2().click()
        print("Click complekt simple")

    """Выбираем комплект револяция"""
    def click_revolution_2(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.get_revolution_2().click()
        print("Click complekt revolution")

    """Кликаем на корзину"""
    def click_cart_2(self):
        self.get_cart_2().send_keys(Keys.PAGE_DOWN)
        self.get_cart_2().send_keys(Keys.RETURN)
        print("Click cart")
    # Methods
    def complekt_product(self):
        self.click_simple()
        time.sleep(5)
        self.click_revolution()
        time.sleep(5)
        self.assert_word(self.get_name_product(), "Samsung Galaxy Z Flip4 F721B 128Gb graphite (графит)")
        self.assert_word(self.get_price_product(), "72 940 ₽")
        self.click_cart()


    def complekt_product_2(self):
        self.click_simple_2()
        time.sleep(5)
        self.click_revolution_2()
        time.sleep(5)
        self.assert_word(self.get_name_product_2(), "Samsung Galaxy Z Flip4 F721B 128Gb blue (голубой)")
        self.assert_word(self.get_price_product_2(), "72 940 ₽")
        self.click_cart_2()

