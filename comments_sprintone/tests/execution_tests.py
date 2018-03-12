import unittest
from selenium import webdriver

from comments_sprintone.resource.path_driver import GetDriver
from comments_sprintone.front.comm_page import CommPage
from comments_sprintone.resource.url_site import PathUrl


class TestExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().get_driver_chrome())
        self.driver.get(PathUrl().get_url_site())
        self.driver.implicitly_wait(5)

    def test_case_one_length(self):
        """Checking error message after filling 50 letters"""
        CommPage(self.driver).create_comment()
        for i in range(51):
            CommPage(self.driver).filling_text_comment("e", False)
        CommPage(self.driver).chose_one_category_comment()
        CommPage(self.driver).save()
        expected_error = 'The maximum length of ' \
                         'Comment Text field is 50 characters'
        actual_error = CommPage(self.driver).check_error_length()
        self.assertEqual(expected_error, actual_error)

    def test_case_second_symbol(self):
        """Checking error message of comment with filling text by symbol"""
        CommPage(self.driver).create_comment()
        CommPage(self.driver).filling_text_comment("!№;", False)
        CommPage(self.driver).save()
        expected_error = "The Comment Text field should " \
                         "contain alphanumeric characters only"
        actual_error = CommPage(self.driver).check_error_symbol()
        self.assertEqual(expected_error, actual_error)

    def test_case_three(self):
        """Checking duplicate button and alert popup without category"""
        CommPage(self.driver).duplicate_comment()
        CommPage(self.driver).check_popup(
            "Please, select one category")

    def test_case_four(self):
        """Checking duplicate button and alert popup
        with select category of main page"""
        CommPage(self.driver).chose_all_category_main()
        CommPage(self.driver).duplicate_comment()
        CommPage(self.driver).check_popup(
            "Please, select one category")

    def test_case_five(self):
        """Checking title name of edit page"""
        CommPage(self.driver).chose_one_category_main()
        CommPage(self.driver).edit_comment()
        actual_name = CommPage(self.driver).check_title_page()
        self.assertIn("Editor", actual_name)

    def test_case_six(self):
        """Checking categories (Cat0, Cat1 etc.) on main page after editing
        P.S. It will been failed!"""
        CommPage(self.driver).chose_one_category_main()
        CommPage(self.driver).edit_comment()
        CommPage(self.driver).chose_all_category_comment()
        CommPage(self.driver).filling_text_comment("EDIT", True)
        CommPage(self.driver).save_and_return()
        CommPage(self.driver).sort_by_number()
        actual_result = CommPage(self.driver).check_categories_main()
        expected_result = ['Cat1; Cat2; Cat3; Cat4; Cat5']
        self.assertIn(expected_result, actual_result)

    def test_case_seven(self):
        """Delete a random comment and confirm this action.
        Waiting for the pop-up request"""
        CommPage(self.driver).chose_one_category_main()
        CommPage(self.driver).delete_comment()
        CommPage(self.driver).confirm_action()

    def test_case_eight(self):
        """Checking message after choosing commentary and clicking a delete"""
        CommPage(self.driver).chose_one_category_main()
        CommPage(self.driver).delete_comment()
        CommPage(self.driver).confirm_action()
        actual_result = CommPage(self.driver).check_successful_popup()
        expected_result = 'Selected comments deleted successfull'
        self.assertEqual(expected_result, actual_result)

    def test_case_nine(self):
        """Checking error message after filling number on comment page"""
        CommPage(self.driver).create_comment()
        CommPage(self.driver).filling_number('1024', False)
        CommPage(self.driver).filling_text_comment("Some text", False)
        CommPage(self.driver).chose_all_category_comment()
        CommPage(self.driver).save()
        expected_error = 'The Number field should contain value from 0 to 999'
        actual_error = CommPage(self.driver).check_error_symbol()
        self.assertEqual(expected_error, actual_error)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
