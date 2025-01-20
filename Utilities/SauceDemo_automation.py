"""
This file contains test logic for Orange HRM automation
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


# importing other files
from TestLocator.locator import SauceDemo_Locator
from TestData.data import SauceDemo_Data
from Utilities.excel_functions import ExcelFunction

# import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from  selenium.common.exceptions import TimeoutException

#import time functionality
from time import sleep
from datetime import datetime

import random

import os


class Saucedemo:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException]
    wait = WebDriverWait(driver, 50, poll_frequency=5, ignored_exceptions= ignored_exceptions)
    
    # logic to open browser with SauceDemo URL
    def url_check(self):
              
        self.driver.get(SauceDemo_Data().url)
        self.driver.maximize_window()
        login_url = self.driver.current_url
        return(login_url)

    # Logic to login
    def login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, SauceDemo_Locator.username_locator))).send_keys(SauceDemo_Data.username)
        print("username")
        self.wait.until(EC.presence_of_element_located((By.ID, SauceDemo_Locator.password_locator))).send_keys(SauceDemo_Data.password)
        print("password")
        self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.login_locator))).click()
        print("Logged in")
        sleep(10)

    # Logic to validate login using cookie
    def login_check_with_cookie(self):
        self.login()
        saucedemo_cookie = self.driver.get_cookie('session-username')
        # print(saucedemo_cookie)
        if saucedemo_cookie['name'] == 'session-username':
            # print(saucedemo_cookie['domain'])
            return saucedemo_cookie['domain']

    # Logic to validate Logout visibility
    def logoutButton_visibility(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.profile_icon_locator))).click()
        print("profile_icon") 
        sleep(5)
        logout_text = self.driver.find_element(By.XPATH, "//a[text()='Logout']" ).text
        # print(logout_text) 
        print("profile_icon") 
        self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))).click()
        print("closed the profile side bar")
        return logout_text
    
    # Logic to validate cart visibility
    def cart_visibility(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        if cart_icon.is_displayed:
            return True
        else:
            return False

    # Logic to fetch all the product ID from the dashboard.
    def Fetching_products_ID(self):
        prodct_list =[]
        index = 1
        # Fetches all 6 product ID using this loop
        while index <= 6:
            product_id = self.driver.find_element(By.XPATH, f"//div[@class='inventory_list']/div[{index}]/div[2]/div[2]/button").get_attribute("id")
            # print(product)
            prodct_list.append(product_id) # add the products to the list
            index += 1
        # print(prodct_list)
        # print(len(prodct_list))
    
        random_product = random.sample(prodct_list, 4) #Selects any 4 product randomly
        # print(len(random_product))
        return(random_product) #returns any 4 product
    
    # Logic to add products to cart randomly
    def Adding_products(self):
        # gets the randomly selected product from the "Fetching_products_ID" function
        id_value = self.Fetching_products_ID()
        for id in id_value:
            button = self.driver.find_element(By.ID, f"{id}")
            button.click()
        sleep(10)
        length = len(id_value)
        return (length)
    
    # Logic to fetch all the product name from the dashboard.
    def fetching_product_Name(self):
        product_name = []
        ind = 1
        while ind <= 6:
            name = self.driver.find_element(By.XPATH, f"//div[@class='inventory_list']/div[{ind}]/div[2]/div/a/div").text
            # print(product)
            product_name.append(name)
            ind += 1
        return(product_name)


    # Logic to fetch all the product name from the cart.
    def fetching_product_Name_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        prouduct_in_cart= []
        inc = 3
        while inc <= 6:
            cart_name = self.driver.find_element(By.XPATH, f"//div[@class='cart_list']/div[{inc}]/div[2]/a/div").text
            print(cart_name)
            prouduct_in_cart.append(cart_name)
            inc += 1
        return(prouduct_in_cart)

    # Logic to checkout the product that are added in the cart and takes screenshot and save it in the folder "Screenshots"
    def checkout(self):
           self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
           print("clicked Checkout button")
           self.wait.until(EC.presence_of_element_located((By.ID, 'first-name'))).send_keys('Berlin')
           print("first name")
           self.wait.until(EC.presence_of_element_located((By.ID, 'last-name'))).send_keys('Pinkmann') 
           print("Last name")
           self.wait.until(EC.presence_of_element_located((By.ID, 'postal-code'))).send_keys('234098') 
           print("Postal code")
           self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
           print("clicked Continue button") #
           self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
           print("clicked FInish button")
           #Folder path
           folder_path = "C:\\Users\\rajap\\OneDrive\\Desktop\\Devi\\01_Python\\14_MainProject\\SauceDemo_Mainproject_DDTF\\Screenshots"
        #    print(f"Folder created at: {os.path.abspath(folder_path)}")
           #creates folder
           os.makedirs("../Screenshots", exist_ok=True)
           print("Folder created")
          # Save the screenshot
           screenshot_path = f"{folder_path}/test_screenshot_1.png"
           self.driver.get_screenshot_as_file(screenshot_path)
           return screenshot_path
                
    # Logic to check the logout Functionality
    def Logout_Functionality(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.profile_icon_locator))).click()
        print("profile_icon")
        self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.logout_locator))).click()
        print("logout")
        sleep(5)
        logout_url = self.driver.current_url
        if logout_url in SauceDemo_Data().url:
            return logout_url
        else:
            return False
         
    # This functions check the login using multiple data present in excel. 
    # Function is constructed using DDT framework
    def loginExcel(self):

        self.excel_file = SauceDemo_Data().excel_file
        self.sheet_number = SauceDemo_Data().sheet_number
        self.excel = ExcelFunction(self.excel_file, self.sheet_number)

        # Get the current date and time
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        self.row = self.excel.row_count()

        for row in range(2,self.row+1):
            username = self.excel.read_data(row, 5)
            password = self.excel.read_data(row, 6)
            
            self.wait.until(EC.presence_of_element_located((By.ID, SauceDemo_Locator.username_locator))).send_keys(username)
            print("username")
            self.wait.until(EC.presence_of_element_located((By.ID, SauceDemo_Locator.password_locator))).send_keys(password)
            print("password")
            self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.login_locator))).click()
            print("Logged in")
            sleep(10)
            if SauceDemo_Data().dashboard_url in self.driver.current_url:
                
                print("url verified")
                self.excel.write_data(row,4,current_date)
                self.excel.write_data(row,7,'Test Passed')
                self.excel.write_data(row,8, current_time)
                # self.driver.back()
                sleep(10)
                self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.profile_icon_locator))).click()
                print("profile_icon")
                self.wait.until(EC.element_to_be_clickable((By.ID, SauceDemo_Locator.logout_locator))).click()
                print("logout")
                self.driver.refresh()
                                    
            elif SauceDemo_Data().url in self.driver.current_url:
                # print("FAILED")
                self.excel.write_data(row,4,current_date)
                self.excel.write_data(row,7,'Test Failed')
                self.excel.write_data(row,8, current_time)
                self.driver.refresh()
                sleep(10)
        return 'Printed'
    
    
    #Finally Shut down
    def shutdown(self):
        self.driver.quit()
        return True