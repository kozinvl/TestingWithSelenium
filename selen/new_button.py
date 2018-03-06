import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net/")

    def test_error_max_length(self):
        """checking max length in text field"""
        error_text = "The maximum length of Comment Text field is 50 characters"
        self.driver.find_element_by_xpath('//*[@id="newbutton"]').click()
        search_comment_field_text = self.driver.find_element_by_name("Text")
        for i in range(49):
            search_comment_field_text.send_keys("x", Keys.ENTER)
        self.driver.find_element_by_name("Number").click()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="errorfield"]/div[1]/span/span').text,
                         error_text)

    def test_add_comment_field_one_category(self):
        """add comment with select one category"""
        search_error_text = 'comment'
        self.driver.find_element_by_id("newbutton").click()
        field_text = self.driver.find_element_by_id("Text")
        field_text.send_keys("comment", Keys.ENTER)
        self.driver.find_element_by_id("Categories").click()
        self.driver.find_element_by_name("CurSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/form/table/thead/tr/th[2]/a').click()
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[3]').text, search_error_text)

    def test_add_comment_field_all_category(self):
        """add comment with select all categories"""
        self.driver.find_element_by_xpath('//*[@id="newbutton"]').click()
        field_text = self.driver.find_element_by_name("Text")
        field_text.send_keys("comment", Keys.ENTER)
        self.driver.find_element_by_name("AllSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        search_category_text = 'Cat0; Cat1; Cat2; Cat3; Cat4; Cat5'
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[5]').text, search_category_text)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
