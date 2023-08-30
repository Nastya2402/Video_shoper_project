import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base



class Samsung_page(Base):
    # url = 'https://video-shoper.ru/catalog/samsung_phone.html'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    all_price = "/html/body/div[2]/main/div[2]/div/div/div[2]/div[1]/div/ul/li[2]/a"
    price = "//*[@id='price-slider-range']/span[1]"
    ram = "/html/body/div[2]/main/div[2]/div/div/div[1]/div[3]/div/form/div[2]/div[1]"
    ram_8g = "//span[@title='8g']"



   #Getters
    # def get_filter_all_price(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_all_price)))


    def get_ram(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(10)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram)))

    def get_ram_8g(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(10)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_8g)))


    # Actions

    """Применяем фильтр по цене """

    def click_all_price(self):
        button_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_price)))
        button_price.click()
        print("Click filter all price")

    """Передвигаем ползунок по цене"""

    def click_price(self):
        action = ActionChains(self.driver)
        price_filtr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))
        action.click_and_hold(price_filtr).move_by_offset(45, 0).release().perform()
        print("Click Price")


    def click_ram(self):
        self.get_ram().click()
        time.sleep(10)
        print("Click ram")

    def click_ram_8g(self):
        self.get_ram_8g().click()
        print("Click ram 8g")


    # Methods
    def f_product(self):
        self.click_all_price()
        self.click_price()
        self.click_ram()
        self.click_ram_8g()

