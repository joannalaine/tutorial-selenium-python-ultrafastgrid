# Source: https://applitools.com/tutorials/selenium-python.html
import os
import pytest
from applitools.selenium import (
    logger,
    FileLogger,
    VisualGridRunner,
    Eyes,
    BatchInfo,
    BrowserType,
    DeviceName,
)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner):
    """
    Basic Eyes setup. It'll abort test if not closed properly.
    """
    eyes = Eyes(runner)
    logger.set_logger(FileLogger("mostrecent.log", mode="w"))
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ["APPLITOOLS_KEY"]
    # Create a new batch info instance and set it to the configuration
    #  Add browsers with different viewports
    #  Add mobile emulation devices in Portrait mode
    eyes.configure.batch = BatchInfo("Ultrafast Batch")
    (
        eyes.configure.add_browser(800, 600, BrowserType.CHROME)
        .add_browser(700, 500, BrowserType.FIREFOX)
        .add_browser(1600, 1200, BrowserType.IE_11)
        .add_browser(1024, 768, BrowserType.EDGE_CHROMIUM)
        .add_browser(800, 600, BrowserType.SAFARI)
        .add_device_emulation(DeviceName.iPhone_X)
        .add_device_emulation(DeviceName.Pixel_2)
    )
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


@pytest.fixture(name="driver", scope="function")
def driver_setup():
    """
    New browser instance per test and quit.
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    # Close the browser.
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results at the end of execution.
    """
    runner = VisualGridRunner(1)
    yield runner
    all_test_results = runner.get_all_test_results()
    print(all_test_results)
