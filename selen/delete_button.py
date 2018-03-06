import unittest
from selenium import webdriver


class DeleteButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")
        self.test_comment = "new comment"

    def test_delete_comment(self):
        """checking delete button"""
        search_successfully_text = "Selected comments deleted successfull"
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").click()
        self.driver.find_element_by_id("Text").clear()
        self.driver.find_element_by_id("Text").send_keys(self.test_comment)
        self.driver.find_element_by_name("AllSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        self.driver.find_element_by_name("SelectedId").click()
        self.driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.driver.find_element_by_xpath("//button/span").click()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="infoField"]').text,
                         search_successfully_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
