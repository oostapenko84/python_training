# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class create_vendor(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def test_create_vendor(self):
        wd = self.wd
        wd.get("https://qa.espresa.com")
        wd.find_element_by_id("public_site_login").click()
        wd.find_element_by_id("login_login").click()
        wd.find_element_by_id("login_login").clear()
        wd.find_element_by_id("login_login").send_keys("admin@admin.com")
        wd.find_element_by_id("login_password").click()
        wd.find_element_by_id("login_password").clear()
        wd.find_element_by_id("login_password").send_keys("12345678")
        wd.find_element_by_id("login_submit").click()

        # [0] - need to refer to any (1-st) element in the array to call function click()
        wd.find_elements_by_xpath("//a[contains(text(), 'Vendors')]")[0].click()
        # add VAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'ADD NEW')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))
        wd.find_elements_by_xpath("//button[contains(text(), 'ADD NEW')]")[0].click()
        wd.find_element_by_id('inputCompanyName').send_keys('Test Company 29')
        wd.find_element_by_id('inputPhone').send_keys('12345')
        # add Location (Address)
        wd.find_element_by_xpath("//div[@class='form-horizontal']//span[.='+ add address']").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[1]/div[2]/input").send_keys("San Francisco")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[2]/div[2]/input").send_keys("San Francisco")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/div[4]/div[2]/input").send_keys("12345")
        wd.find_element_by_xpath("//div[@class='modal-content']//button[.='ADD']").click()
        wd.find_element_by_id('inputWebSite').send_keys('www.test.com')
        wd.find_element_by_id('inputDescription').send_keys('test')
        # enter Administration Staff
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[1]/input").send_keys(
            "VAD First Name 29")
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[1]/div[2]/input").send_keys(
            "VAD Last Name 29")
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[2]/div[1]/input").send_keys(
            "test29@test.com")
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='form-horizontal']/div[14]/div[3]/div[1]/div/div[2]/input").send_keys(
            "12345678")
        wd.find_element_by_xpath("//div[@class='nav-bar-button']//button[.='SAVE & EXIT']").click()
        # upload Avatar
        # wd.find_element_by_css_selector("input.btn-upload.firepath-matching-node").click()
        # wd.find_element_by_css_selector("button.btn.cancel").click()
        # wd.find_element_by_class_name("btn-upload").send_keys("C:/Users/olga.ostapenko/Desktop/Pics/test2.jpg")

    def tearDown(self):
        print('OK')
        # self.wd.quit()


if __name__ == '__main__':
    unittest.main()
