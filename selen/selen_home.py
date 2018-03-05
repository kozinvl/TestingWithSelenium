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
        search_error_text = "The maximum length of Comment Text field is 50 characters"
        self.driver.find_element_by_xpath('//*[@id="newbutton"]').click()
        search_comment_field_text = self.driver.find_element_by_name("Text")
        for i in range(49):
            search_comment_field_text.send_keys("x", Keys.ENTER)
        self.driver.find_element_by_name("Number").click()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="errorfield"]/div[1]/span/span').text,
                         search_error_text)

    def test_new_comment_field_one_category(self):
        search_error_text = 'nnnnn'
        new_comment_button = self.driver.find_element_by_xpath('//*[@id="newbutton"]')
        new_comment_button.click()
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

    def test_new_comment_field_all_category(self):
        new_comment_button = self.driver.find_element_by_xpath('//*[@id="newbutton"]')
        new_comment_button.click()
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
        self.test_comment = "new comment"
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
        change_text_field = "edit"
        self.driver.find_element_by_id("Text").send_keys(change_text_field)
        search_string = self.driver.find_element_by_id("Text").get_attribute("value")
        time.sleep(2)
        self.assertEqual(search_string, change_text_field)

    def test_delete(self):
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

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
