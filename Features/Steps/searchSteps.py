from Helpers.requestsHelper import search_endpoint_url, save_response
from Helpers.searchHelper import check_value_in_attribute, check_search_string_in_page
from Utilities.TestBase import TestBase
import requests
from behave import given, when, then


@given('A Client of the API')
def step_given_client(context):
    pass


@when('A search for pages containing "{search_string}" is executed')
def step_search_on_a_page(context, search_string):
    params = {"q": search_string, "limit": TestBase.SearchLimitMax}
    response = requests.get(search_endpoint_url, params=params)
    context.response = response.json()


@then('A page with the "{attribute}" "{expected_value}" is found')
def step_text_found_in_attribute(context, attribute, expected_value):
    text_found = check_value_in_attribute(context.response["pages"], attribute, expected_value)
    assert text_found, f'Text "{expected_value}" not found in "{attribute}"'


@given('The result for "{query}" search contains "{search_text}"')
def search_text_found(context, query, search_text):
    params = {"q": query, "limit": TestBase.SearchLimitMax}
    response = requests.get(search_endpoint_url, params=params)
    context.response = response.json()
    check_search_string_in_page(context.response["pages"], search_text)
    save_response(context.response)
