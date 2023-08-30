import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base



class Samsung_galaxy_Z_flip_4_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    galaxy_Z_flip_4 = "//a[@data-product-id='5003702']"
    galaxy_Z_flip_4_blue = "//a[@data-product-id='5003715']"
   #Getters
    def get_galaxy_Z_flip_4(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(10)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.galaxy_Z_flip_4)))

    def get_galaxy_Z_flip_4_blue(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(10)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.galaxy_Z_flip_4_blue)))

    # Actions

    """Добавляем товар в корзину"""

    def click_galaxy_Z_flip_4(self):
        self.get_galaxy_Z_flip_4().click()
        print("Click on Samsung galaxy Z flip 4")

    def click_galaxy_Z_flip_4_blue(self):
        self.get_galaxy_Z_flip_4_blue().click()
        print("Click on Samsung galaxy Z flip 4 blue")
    # Methods
    def galaxy_product(self):
        self.click_galaxy_Z_flip_4()

    def galaxy_product_2(self):
        self.click_galaxy_Z_flip_4_blue()