import unittest
from comments_sprintone.front.path_to_object import New_Comm, Other, \
    Delete, Duplicate, Edit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestFunctional(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def create_comment(self):
        """click on new button and move to new comment page"""
        comment = self.driver.find_element_by_id(
            New_Comm().get_create_button())
        comment.click()

    def duplicate_comment(self):
        duplicate_comment = self.driver.find_element_by_xpath(
            Duplicate().get_duplcate_button())
        duplicate_comment.click()

    def edit_comment(self):
        """click on edit button and move to edit page"""
        edit_comment = self.driver.find_element_by_xpath(
            Edit().get_edit_button())
        edit_comment.click()

    def delete_comment(self):
        """click on delete button and move to edit page"""
        delete_comment = self.driver.find_element_by_xpath(
            Delete().get_delete_button())
        delete_comment.click()

    def confirm_action(self):
        """confirmation positive action with button (yes)"""
        confirm_btn = self.driver.find_element_by_xpath(
            Delete().get_confirmative_button())
        confirm_btn.click()

    def filling_text_comment(self, add_text: str, is_cleared: False):
        """filling comment field by letters"""
        text_field = self.driver.find_element_by_id(New_Comm().send_text())
        if is_cleared:
            text_field.clear()
        text_field.send_keys(add_text, Keys.ENTER)

    def filling_number(self, add_number: str, is_cleared: False):
        """filling comment field by number"""
        number_field = self.driver.find_element_by_id(
            New_Comm().send_number())
        number_field.click()
        if is_cleared:
            number_field.clear()
        number_field.send_keys(add_number, Keys.ENTER)

    def save(self):
        """save all data on new comment page"""
        save_btn = self.driver.find_element_by_xpath(
            Other().get_save_btn())
        save_btn.click()

    def save_and_return(self):
        """save and return to main page"""
        save_return_btn = self.driver.find_element_by_xpath(
            Other().get_save_return_btn())
        save_return_btn.click()

    def chose_one_category_comment(self):
        """chose category on new comment page"""
        one_category = self.driver.find_element_by_xpath(
            New_Comm().get_category_cat())
        one_category.click()
        one_category.click()
        confirm_category = self.driver.find_element_by_name(
            New_Comm().confirm_one_category())
        confirm_category.click()

    def chose_all_category_comment(self):
        """chose all category on new comment page"""
        self.driver.find_element_by_name(
            New_Comm().confirm_all_category()).click()

    def check_error_length(self, expected_error):
        comment_text = self.driver.find_element_by_xpath(
            Other().alert_length()).text
        self.assertEqual(comment_text, expected_error)

    def check_error_symbol(self, expected_error):
        comment_text = self.driver.find_element_by_id(
            Other().alert_symbol()).text
        self.assertEqual(comment_text, expected_error)

    def check_popup(self, expected_text):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert expected_text in alert.text

    def check_successful_popup(self):
        successful_txt = self.driver.find_element_by_id(
            Delete().get_successful_text())
        return successful_txt.text

    def chose_all_category_main(self):
        """chose all category on main page"""
        all_category = self.driver.find_elements_by_name(
            Other().all_category_main())
        for each_category in all_category:
            each_category.click()

    def chose_one_category_main(self):
        """chose one category on main page"""
        one_category = self.driver.find_element_by_xpath(
            Other().one_random_cat())
        one_category.click()

    def check_title_page(self, text_page):
        self.assertIn(text_page, self.driver.title)

    def sort_by_number(self):
        """sorting comments by number on main page"""
        sort_number = self.driver.find_element_by_xpath(
            New_Comm().sort_by_numb())
        sort_number.click()

    def check_categories_main(self) -> list:
        web_elements = self.driver.find_elements_by_class_name(
            New_Comm().get_category_text())
        web_text_elements = [web_element.text for web_element in web_elements]
        actual_result = [each.split(",") for each in web_text_elements]
        return actual_result
