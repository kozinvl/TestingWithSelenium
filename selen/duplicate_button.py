import unittest
from selenium import webdriver


class DuplicateButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")

    def test_duplicate(self):
        """checking duplicate button"""
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").send_keys("new")
        self.driver.find_element_by_xpath("(//input[@id='Categories'])[2]").click()
        self.driver.find_element_by_name("CurSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        self.driver.find_element_by_name("SelectedId").click()
        self.driver.find_element_by_xpath("//input[@value='Duplicate...']").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        search_duplicate = 'Copy of new'
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[2]/td[3]').text, search_duplicate)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
