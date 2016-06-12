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


class create_company(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def test_create_company(self):
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
        wd.find_elements_by_xpath("//a[contains(text(), 'Companies')]")[0].click()
        # add CAD
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'ADD NEW')]")))
        WebDriverWait(wd, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.popup-loader")))
        wd.find_elements_by_xpath("//button[contains(text(), 'ADD NEW')]")[0].click()
        wd.find_element_by_id('inputCompanyName').send_keys('Test Company 18')
        wd.find_element_by_id("inputFirstName").click()
        wd.find_element_by_id("inputFirstName").clear()
        wd.find_element_by_id("inputFirstName").send_keys("Company First Name 18")
        wd.find_element_by_id("inputLastName").click()
        wd.find_element_by_id("inputLastName").clear()
        wd.find_element_by_id("inputLastName").send_keys("Company Last Name 18")
        wd.find_element_by_id("inputLogin").click()
        wd.find_element_by_id("inputLogin").clear()
        wd.find_element_by_id("inputLogin").send_keys("test18@test.com")
        wd.find_element_by_id("inputPhone").click()
        wd.find_element_by_id("inputPhone").clear()
        wd.find_element_by_id("inputPhone").send_keys("12345678")
        wd.find_element_by_id("inputFax").click()
        wd.find_element_by_id("inputFax").clear()
        wd.find_element_by_id("inputFax").send_keys("12345678")
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
        self.wd.implicitly_wait(200)
        wd.find_element_by_id('inputSite').send_keys('www.test.com')
        wd.find_element_by_id('inputDescription').send_keys('test')
        wd.find_element_by_id("inputPoints").send_keys("1000")
        wd.find_element_by_xpath("//div[@class='nav-bar-button']//button[.='SAVE & EXIT']").click()

    def tearDown(self):
        print('OK')
        # self.wd.quit()


if __name__ == '__main__':
    unittest.main()