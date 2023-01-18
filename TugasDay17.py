import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #Test Auto 1 Tampilkan Website    
    def test_Login_a_show(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com") # buka situs
        driver.maximize_window()
        time.sleep(3)

    #Test Auto 2 Click login tapi tanpa input username dan password
    def test_Login_b_empty(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com") # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click() #langsung login
        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error").text
        self.assertEqual(response_message, 'Epic sadface: Username is required')
        time.sleep(3)

    #Test Auto 3 Error salah pas dan akun
    def test_login_c_with_wrong_email_and_password(self): 
        # steps
        driver = self.driver #buka web browser
        driver.get("https://www.saucedemo.com") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input").send_keys("admin") # isi username
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123abclolos") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click() # klik tombol login
        time.sleep(1)
        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')
        time.sleep(3)

unittest.main()
