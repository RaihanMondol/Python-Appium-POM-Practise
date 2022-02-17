import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By


class test_Appium(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['platformName'] = 'Android'
        self.dc['automationName'] = 'UiAutomator2'
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['udid'] = 'emulator-5554'
        self.dc['app'] = 'C:\\Users\\LENOVO\\Downloads\\com.bdjobs.app-v2.8.0.3.apk'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)

    def test(self):
        self.driver.find_element(By.ID, "com.bdjobs.app:id/btn_next").click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(5)
        self.driver.find_element(By.ID, 'com.bdjobs.app:id/profileIMGV').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'com.bdjobs.app:id/usernameTIET').send_keys("raihanmondolbd@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.ID, 'com.bdjobs.app:id/nextButtonFAB').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'com.bdjobs.app:id/passwordTIET').send_keys("123456789")
        time.sleep(3)
        self.driver.find_element(By.ID, 'com.bdjobs.app:id/nextButtonFAB').click()


    def tearDown(self):
        # self.driver.quit()
        print("pass")


if __name__ == '__main__':
    unittest.main()
