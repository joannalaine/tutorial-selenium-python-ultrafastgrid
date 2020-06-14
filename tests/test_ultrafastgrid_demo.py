# Source: https://applitools.com/tutorials/selenium-python.html
from applitools.selenium import Target
from pages.login import LoginPage


def check_login_flow(driver, eyes, url):
    try:
        login_page = LoginPage(driver, url)
        # Navigate to the url we want to test
        login_page.load()

        # Call Open on eyes to initialize a test session
        eyes.open(
            driver, "Demo App", "Ultrafast grid demo", {"width": 800, "height": 600}
        )

        # check the login page with fluent api, see more info here
        # https://applitools.com/docs/topics/sdk/the-eyes-sdk-check-fluent-api.html
        eyes.check("", Target.window().fully().with_name("Login page"))

        login_page.log_in()

        # Check the app page
        eyes.check("", Target.window().fully().with_name("App page"))

        # Call Close on eyes to let the server know it should display the results
        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)


def test_tutorial_v1(driver, eyes):
    check_login_flow(driver, eyes, "https://demo.applitools.com")


def test_tutorial_v2(driver, eyes):
    check_login_flow(driver, eyes, "https://demo.applitools.com/index_v2.html")
