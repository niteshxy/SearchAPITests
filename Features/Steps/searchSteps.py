from Helpers.searchHelper import check_value_in_attribute
from Utilities.TestBase import TestBase
import requests
from behave import given, when, then

search_api_url = f"{TestBase.BaseUrl}{TestBase.ApiVersion}/wikipedia/{TestBase.Languages[0]}{TestBase.SEARCH_ENDPOINT}"


@given('A Client of the API')
def step_given_client(context):
    pass


@when('A search for pages containing "{search_string}" is executed')
def step_search_on_a_page(context, search_string):
    params = {"q": search_string, "limit": TestBase.SearchLimitMax}
    response = requests.get(search_api_url, params=params)
    context.response = response.json()


@then('A page with the "{attribute}" "{expected_value}" is found')
def step_text_found_in_attribute(context, attribute, expected_value):
    text_found = check_value_in_attribute(context.response["pages"],attribute, expected_value)
    # AttributeFound = False
    # for page in context.response["pages"]:
    #     if page[attribute] == expected_value:
    #         AttributeFound = True
    #         break
    assert text_found,f'Text "{expected_value}" not found in "{attribute}"'
