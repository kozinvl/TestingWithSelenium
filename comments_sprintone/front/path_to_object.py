"""Classes wich returning location of required elements"""
import random


class NewComm(object):
    CREATE_BUTTON = "newbutton"
    SEND_TEXT = "Text"
    SEND_NUMBER = "Number"
    ALL_CATEGORIES = "AllSelect"
    ONE_CATEGORY = "CurSelect"
    TEXT_IN_CATEGORIES = "categorycolumn"
    SORT_BY_NUMBER = ".//*[@class='webgrid-header']//a[text()='Number']"

    def get_category_cat(self) -> str:
        """chose random category on the new comm page"""
        random_digit = random.randint(2, 4)
        return ".//*[@id='Categories'][@name='Categories']" \
               "[@value = {digit}]".format(digit=random_digit)


class Edit(object):
    EDIT_BUTTON = "//input[@value='Edit..']"


class Duplicate(object):
    DUPLICATE_BUTTON = "//input[@value='Duplicate...']"


class Delete(object):
    DELETE_BUTTON = "//input[@value='Delete']"
    CONFIRMATION_BUTTON = "//*[text()='Yes']"
    SUCCESSFUL_TEXT = "infoField"


class Other(object):
    SAVE_RETURN_BUTTON = ".//*/input[@value='Save & Return']"
    SAVE_BUTTON = ".//*/input[@value='Save']"
    ALL_CATEGORIES_MAIN = "SelectedId"
    ERROR_LENGTH = "//SPAN[@htmlfor='Text']"
    ERROR_SYMBOL = "errorfield"
    RANDOM_CAT_START = 1
    RANDOM_CAT_FINISH = 10

    def one_random_cat(self) -> str:
        """Choosing random category main page"""
        path_checkbox = "(//INPUT[@type='checkbox'])"
        random_category = random.randint(Other.RANDOM_CAT_START,
                                         Other.RANDOM_CAT_FINISH)
        return "{}[{}]".format(path_checkbox, random_category)
