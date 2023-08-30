import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.choise_complekt_page import Choise_complekt_page
from pages.finish_cart_page import Finish_cart_page
from pages.main_page import Main_page
from pages.samsung_galaxy_Z_flip_4_page import Samsung_galaxy_Z_flip_4_page
from pages.samsung_page import Samsung_page

@pytest.mark.run(order=2)
def test_buy_products_1(set_up, set_group):
    # options = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Nasty\\PycharmProjects\\resourse\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)


    print("Start Test 1")

    mp = Main_page(driver)
    mp.choise_product()
    sp = Samsung_page(driver)
    sp.f_product()
    gf = Samsung_galaxy_Z_flip_4_page(driver)
    gf.galaxy_product()
    time.sleep(10)
    cc = Choise_complekt_page(driver)
    cc.complekt_product()
    fp = Finish_cart_page(driver)
    fp.finish_product()


    print("Finish Test 1")
    time.sleep(10)
    driver.quit()

@pytest.mark.run(order=1)
def test_buy_products_2(set_up, set_group):
    # options = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Nasty\\PycharmProjects\\resourse\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)


    print("Start Test 2")

    mp = Main_page(driver)
    mp.choise_product()
    sp = Samsung_page(driver)
    sp.f_product()
    gf = Samsung_galaxy_Z_flip_4_page(driver)
    gf.galaxy_product_2()
    time.sleep(10)
    cc = Choise_complekt_page(driver)
    cc.complekt_product_2()
    fp = Finish_cart_page(driver)
    fp.finish_product_2()


    print("Finish Test 2")
    time.sleep(10)
    driver.quit()