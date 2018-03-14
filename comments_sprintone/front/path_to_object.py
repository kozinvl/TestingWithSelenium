"""Classes wich returning location of required elements"""
import random


class NewComm(object):
    CREATE_BUTTON = "newbutton"
    SEND_TEXT = "Text"
    SEND_NUMBER = "Number"
    ALL_CATEGORIES = "AllSelect"
    ONE_CATEGORY = "CurSelect"
    TEXT_CATEGORIES = "categorycolumn"
    SORT_NUMBER = ".//*[@class='webgrid-header']//a[text()='Number']"
    RANDOM_CATEGORY_START = 2
    RANDOM_CATEGORY_FINISH = 4

    @staticmethod
    def choose_random_category_cat() -> str:
        """choosing random category on the new comm page"""
        random_digit = random.randint(NewComm.RANDOM_CATEGORY_START,
                                      NewComm.RANDOM_CATEGORY_FINISH)
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

    @staticmethod
    def choose_one_random_cat() -> str:
        """Choosing random category main page"""
        path_checkbox = "(//INPUT[@type='checkbox'])"
        random_category = random.randint(Other.RANDOM_CAT_START,
                                         Other.RANDOM_CAT_FINISH)
        return "{}[{}]".format(path_checkbox, random_category)
