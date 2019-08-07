
from behave import given, when, then # pylint: disable=no-name-in-module
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig

# start of step definitions

@given('I go to the site "{site}"')
def go_to_url(context, site):
  
    #putting break point
    url = urlconfig.URLCONFIG.get(site)

    print("Navigating to the site: {}".format(url))

    context.driver = webcommon.go_to(url)

@then('the page title should be "{expected_title}"')
def verify_home_page_title(context, expected_title):
    webcommon.assert_page_title(context,expected_title)

