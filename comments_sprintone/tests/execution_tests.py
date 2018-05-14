import unittest
from selenium import webdriver

from comments_sprintone.resource.path_driver import GetDriver
from comments_sprintone.front.comm_page import CommentsPage
from comments_sprintone.resource.url_site import PathUrl


class TestExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        self.driver.get(PathUrl().URL_SITE)
        self.driver.implicitly_wait(5)

    def test_comment_text_field_length(self):
        """Checking error message after filling more than 50 letters"""
        comment_page = CommentsPage(self.driver)
        comment_page.click_create_comment()
        comment_page.filling_text_comment("e" * 51, False)
        comment_page.chose_one_category_comment()
        comment_page.save()
        expected_error = 'The maximum length of ' \
                         'Comment Text field is 50 characters'
        actual_error = comment_page.get_error_length()
        self.assertEqual(expected_error, actual_error)

    def test_comment_symbol_field_error(self):
        """Checking error message of comment with filling text by symbol"""
        comment_page = CommentsPage(self.driver)
        comment_page.click_create_comment()
        comment_page.filling_text_comment("!@", False)
        comment_page.save()
        expected_error = "The Comment Text field should " \
                         "contain alphanumeric characters only"
        actual_error = comment_page.get_error_symbol()
        self.assertEqual(expected_error, actual_error)

    def test_duplicate_alert(self):
        """Checking duplicate button and alert popup without category"""
        comment_page = CommentsPage(self.driver)
        comment_page.click_duplicate_comment()
        expected_alert = "Please, select one category"
        actual_alert = comment_page.get_check_popup()
        assert expected_alert in actual_alert

    def test_duplicate_alert_all_category(self):
        """Checking duplicate button and alert popup
        with select category of main page"""
        comment_page = CommentsPage(self.driver)
        comment_page.choose_all_categories_main()
        comment_page.click_duplicate_comment()
        expected_alert = "Please, select one category"
        actual_alert = comment_page.get_check_popup()
        assert expected_alert in actual_alert

    def test_edit_page_title_name(self):
        """Checking title name of edit page"""
        comment_page = CommentsPage(self.driver)
        comment_page.choose_one_category_main()
        comment_page.click_edit_comment()
        actual_name = comment_page.get_name_title_page()
        self.assertIn("Editor", actual_name)

    def test_main_categories(self):
        """Checking categories (Cat0, Cat1 etc.) on main page after editing
        P.S. It will been failed!"""
        comment_page = CommentsPage(self.driver)
        comment_page.choose_one_category_main()
        comment_page.click_edit_comment()
        comment_page.choose_all_category_comment()
        comment_page.filling_text_comment("EDIT", True)
        comment_page.save_return()
        comment_page.sort_number()
        actual_result = comment_page.get_categories_main()
        expected_result = ['Cat1; Cat2; Cat3; Cat4; Cat5']
        self.assertIn(expected_result, actual_result)

    def test_delete_comment_popup(self):
        """Delete a random comment and confirm this action.
        Waiting for the pop-up request"""
        comment_page = CommentsPage(self.driver)
        comment_page.choose_one_category_main()
        comment_page.delete_comment()
        comment_page.confirm_action()

    def test_delete_comment_error(self):
        """Checking message after choosing commentary and clicking a delete"""
        comment_page = CommentsPage(self.driver)
        comment_page.choose_one_category_main()
        comment_page.delete_comment()
        comment_page.confirm_action()
        actual_result = comment_page.get_successful_popup()
        expected_result = 'Selected comments deleted successfull'
        self.assertEqual(expected_result, actual_result)

    def test_comment_number_field_error(self):
        """Checking error message after filling number on comment page"""
        comment_page = CommentsPage(self.driver)
        comment_page.click_create_comment()
        comment_page.filling_number('1024', False)
        comment_page.filling_text_comment("Some text", False)
        comment_page.choose_all_category_comment()
        comment_page.save()
        expected_error = 'The Number field should contain value from 0 to 999'
        actual_error = comment_page.get_error_symbol()
        self.assertEqual(expected_error, actual_error)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
