import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EditButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")

    def test_edit(self):
        """checking edit button"""
        self.test_comment = "new comment"
        change_text_field = "edit"
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").send_keys(self.test_comment, Keys.ENTER)
        self.driver.find_element_by_name("AllSelect").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/'
                                          'form/table/thead/tr/th[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/'
                                          'form/table/tbody/tr[1]/td[1]/input[1]').click()
        self.driver.find_element_by_xpath('//*[@id="command-navigation"]/input[2]').click()
        self.driver.find_element_by_id("Text").clear()
        self.driver.find_element_by_id("Text").send_keys(change_text_field)
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        search_string = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]'
                                                          '/form/table/tbody/tr[1]/td[3]').text
        self.assertEqual(search_string, change_text_field)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
