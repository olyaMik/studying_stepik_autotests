



class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_page(self):
        self.browser.get(self.url)

