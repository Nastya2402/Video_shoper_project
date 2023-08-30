from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base


class Main_page(Base):
    url = 'https://video-shoper.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    catalog = "/html/body/div[2]/header/div[2]/div/div/a/i"
    samsung = "//a[@href='/catalog/samsung_phone.html']"
    header_phone = "//a[@class='header-phone']"

   #Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_samsung(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung)))

    def get_header_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_phone)))


    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print("Click Catalog")


    def click_samsung(self):
        self.get_samsung().click()
        print("Click samsung")


    # Methods
    def choise_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_word(self.get_header_phone(), "+7 (495) 648-68-08")
        self.click_catalog()
        self.click_samsung()
