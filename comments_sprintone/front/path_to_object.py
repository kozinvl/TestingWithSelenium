"""Classes wich returning location of required elements"""
import random


class NewComm(object):
    CREATE_BUTTON = "newbutton"

    def send_text(self) -> str:
        return "Text"

    def send_number(self) -> str:
        return "Number"

    def get_error_length(self) -> str:
        return ".field-validation-error>span"

    def get_category_cat(self) -> str:
        random_digit = random.randint(2, 4)
        return ".//*[@id='Categories'][@name='Categories']" \
               "[@value = {digit}]".format(digit=random_digit)

    def confirm_all_category(self):
        return "AllSelect"

    def confirm_one_category(self) -> str:
        return "CurSelect"

    def sort_by_numb(self):
        return ".//*[@class='webgrid-header']//a[text()='Number']"

    def get_category_text(self):
        return "categorycolumn"


class Edit(object):
    EDIT_BUTTON = "//input[@value='Edit..']"


class Duplicate(object):
    DUPLICATE_BUTTON = "//input[@value='Duplicate...']"


class Delete(object):

    def get_delete_button(self):
        return "//input[@value='Delete']"

    def get_confirmative_button(self):
        return "//*[text()='Yes']"

    def get_successful_text(self):
        return "infoField"


class Other(object):
    SAVE_RETURN_BUTTON = ".//*/input[@value='Save & Return']"
    SAVE_BUTTON = ".//*/input[@value='Save']"
    ALL_CATEGORIES_MAIN = "SelectedId"
    ERROR_LENGTH = "//SPAN[@htmlfor='Text']"
    ERROR_SYMBOL = "errorfield"

    def one_random_cat(self) -> str:
        """Choosing random category main page"""
        path_box = "(//INPUT[@type='checkbox'])"
        random_category = random.randint(1, 10)
        return "{}[{}]".format(path_box, random_category)
