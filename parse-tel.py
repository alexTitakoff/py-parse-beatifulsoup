from selenium import webdriver


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def navigate(self):
        self.driver.get('https://www.avito.ru/ryazan/telefony/iphone_16_gb_silver_1156788230')

        button = self.driver.find_element_by_class_name('item-phone-number')
        button.click()

        self.take_screenshot()

def main():
    print 'start'
    b = Bot()


if __name__ == '__main__':
    main()
