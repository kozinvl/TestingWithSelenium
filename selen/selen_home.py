import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewComment(unittest.TestCase):
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
        search_error_text = 'nnnnn'
        self.driver.find_element_by_xpath('//*[@id="newbutton"]').click()
        field_text = self.driver.find_element_by_name("Text")
        for i in range(5):
            field_text.send_keys("n", Keys.ENTER)
        self.driver.find_element_by_name("Categories").click()
        self.driver.find_element_by_name("CurSelect").click()
        self.driver.find_element_by_xpath('//*[@id="editor-navigation"]/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/form/table/thead/tr/th[2]/a').click()
        print(self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[3]').text)
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[3]').text, search_error_text)

    def test_add_comment_field_all_category(self):
        """add comment with select all categories"""
        self.driver.find_element_by_xpath('//*[@id="newbutton"]').click()
        field_text = self.driver.find_element_by_name("Text")
        for i in range(5):
            field_text.send_keys("n", Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="categoryselector"]/div[2]/input[1]').click()
        self.driver.find_element_by_xpath('//*[@id="editor-navigation"]/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/form/table/thead/tr/th[2]/a').click()
        search_category_text = 'Cat0; Cat1; Cat2; Cat3; Cat4; Cat5'
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[5]').text, search_category_text)
        time.sleep(2)

    def test_duplicate(self):
        """checking duplicate button"""
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").send_keys("nnnnn")
        self.driver.find_element_by_xpath("(//input[@id='Categories'])[2]").click()
        self.driver.find_element_by_name("CurSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        self.driver.find_element_by_name("SelectedId").click()
        self.driver.find_element_by_xpath("//input[@value='Duplicate...']").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        search_duplicate = 'Copy of nnnnn'
        self.assertEqual(self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[2]/td[3]').text, search_duplicate)
        time.sleep(1)

    def test_edit(self):
        """checking edit button"""
        self.test_comment = "new comment"
        change_text_field = "edit"
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").send_keys(self.test_comment, Keys.ENTER)
        self.driver.find_element_by_name("AllSelect").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="editor-navigation"]/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/'
                                          'form/table/thead/tr/th[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/'
                                          'form/table/tbody/tr[1]/td[1]/input[1]').click()
        self.driver.find_element_by_xpath('//*[@id="command-navigation"]/input[2]').click()
        self.driver.find_element_by_id("Text").clear()

        self.driver.find_element_by_id("Text").send_keys(change_text_field)
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        time.sleep(3)
        search_string = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]'
                                                          '/form/table/tbody/tr[1]/td[3]').text
        self.assertEqual(search_string, change_text_field)

    def test_delete_comment(self):
        """checking delete button"""
        search_successfully_text = "Selected comments deleted successfull"
        self.driver.find_element_by_id("newbutton").click()
        self.driver.find_element_by_id("Text").click()
        self.driver.find_element_by_id("Text").clear()
        self.driver.find_element_by_id("Text").send_keys("new")
        self.driver.find_element_by_name("AllSelect").click()
        self.driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        self.driver.find_element_by_link_text("Number").click()
        self.driver.find_element_by_name("SelectedId").click()
        self.driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.driver.find_element_by_xpath("//button/span").click()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="infoField"]').text,
                         search_successfully_text)

    def test_delete_comments(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
