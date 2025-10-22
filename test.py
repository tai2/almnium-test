from time import sleep
import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from alumnium import Alumni


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        options = XCUITestOptions()
        options.platform_version = "18.6"
        options.device_name = "iPhone 16 Pro"
        options.app = "./Wikipedia.zip"
        options.new_command_timeout = 60 * 20
        appium_server_url = "http://localhost:4723"
        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.al = Alumni(self.driver)

    def tearDown(self) -> None:
        pass
        # if self.driver:
        #     self.driver.quit()

    def test_something(self) -> None:
        self.al.do("Skip the start screen")
        self.al.do("Go to search screen")

        sleep(3)
        self.driver.save_screenshot("screenshot.png")


if __name__ == "__main__":
    unittest.main()
