from selenium import webdriver

def go_to(url, browser_type=None):

    if not browser_type:
        # create instance of Firefox driver the browser type is not specified
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        # create instance of the Chrome driver
        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    driver.get(url)

    return driver

def assert_page_title(context, expected_title):
    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)

