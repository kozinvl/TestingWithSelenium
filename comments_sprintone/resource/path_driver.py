import os


class GetDriver(object):
    def get_driver_chrome(self):
        return os.path.dirname(__file__) + '/chromedriver.exe'

    def get_driver_firefox(self):
        return os.path.dirname(__file__) + '/geckodriver.exe'
