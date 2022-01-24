import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_make_parametrize_id(config, val): return repr(val)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")  
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print(f"\nstart {browser_name} for test with language:{user_language}..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nstart {browser_name} for test with language:{user_language}..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

    #
