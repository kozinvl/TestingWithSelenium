import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from comments_sprintone.resource.path_driver import GetDriver
from comments_sprintone.tests.tests_function import TestFunctional
from comments_sprintone.resource.url_site import PathUrl


class TestExecution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().get_driver_chrome())
        self.driver.get(PathUrl().get_url_site())
        self.driver.implicitly_wait(5)

    def test_case_first_length(self):
        """Checking error message after filling 50 letters"""
        TestFunctional(self.driver).create_comment()
        for i in range(50):
            TestFunctional(self.driver).filling_text_comment("e", False)
        TestFunctional(self.driver).chose_one_category_comment()
        TestFunctional(self.driver).save()
        expected_error_text = 'The maximum length of ' \
                              'Comment Text field is 50 characters'
        TestFunctional(self.driver).check_error_length(expected_error_text)

    def test_case_second_symbol(self):
        """Checking error message of comment with filling text by symbol"""
        TestFunctional(self.driver).create_comment()
        TestFunctional(self.driver).filling_text_comment("!№;", False)
        TestFunctional(self.driver).save()
        expected_error_text = "The Comment Text field should " \
                              "contain alphanumeric characters only"
        TestFunctional(self.driver).check_error_symbol(expected_error_text)

    def test_case_three(self):
        """Checking duplicate button and alert popup without category"""
        TestFunctional(self.driver).duplicate_comment()
        TestFunctional(self.driver).check_popup(
            "Please, select one category")

    def test_case_four(self):
        """Checking duplicate button and alert popup
        with select category of main page"""
        TestFunctional(self.driver).chose_all_category_main()
        TestFunctional(self.driver).duplicate_comment()
        TestFunctional(self.driver).check_popup(
            "Please, select one category")

    def test_case_five(self):
        """Checking title name of edit page"""
        TestFunctional(self.driver).chose_one_category_main()
        TestFunctional(self.driver).edit_comment()
        TestFunctional(self.driver).check_title_page("Editor")

    def test_case_six(self):
        """Checking categories (Cat0, Cat1 etc.) on main page after editing
        P.S. It will been failed!"""
        TestFunctional(self.driver).chose_one_category_main()
        TestFunctional(self.driver).edit_comment()
        TestFunctional(self.driver).chose_all_category_comment()
        TestFunctional(self.driver).filling_text_comment("EDIT", True)
        TestFunctional(self.driver).save_and_return()
        TestFunctional(self.driver).sort_by_number()
        actual_result = TestFunctional(self.driver).check_categories_main()
        expected_result = ['Cat1; Cat2; Cat3; Cat4; Cat5']
        self.assertIn(expected_result, actual_result)

    def test_case_seven(self):
        """Delete a random comment and confirm this action.
        Waiting for the pop-up request"""
        TestFunctional(self.driver).chose_one_category_main()
        TestFunctional(self.driver).delete_comment()
        TestFunctional(self.driver).confirm_action()

    def test_case_eight(self):
        """Checking message after choosing commentary and clicking a delete"""
        TestFunctional(self.driver).chose_one_category_main()
        TestFunctional(self.driver).delete_comment()
        TestFunctional(self.driver).confirm_action()
        actual_result = TestFunctional(self.driver).check_successful_popup()
        expected_result = 'Selected comments deleted successfull'
        self.assertEqual(expected_result, actual_result)

    def test_case_nine(self):
        """Checking error message after filling number on comment page"""
        TestFunctional(self.driver).create_comment()
        TestFunctional(self.driver).filling_number('1024', False)
        TestFunctional(self.driver).filling_text_comment("Some text", False)
        TestFunctional(self.driver).chose_all_category_comment()
        TestFunctional(self.driver).save()
        expected_error = 'The Number field should contain value from 0 to 999'
        TestFunctional(self.driver).check_error_symbol(expected_error)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


















    # firefox_capabilities = DesiredCapabilities.FIREFOX
    # firefox_capabilities['marionette'] = True
    # self.driver = webdriver.Firefox(capabilities=firefox_capabilities)
