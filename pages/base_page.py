class BasePage:

    def __init__(self, page):
        self.page = page

    def open_page(self, link):
        self.page.goto(link)

    def get_url(self):
        return self.page.url

    def reload_page(self):
        self.page.reload()

    def get_back(self):
        self.page.go_back()

    def correct_direction(self, target_url):
        assert self.page.url == target_url

    def make_screenshot(self, save_name):
        self.page.screenshot(path=save_name)

    def page_moving(self, y, x):
        self.page.mouse.wheel(y, x)
