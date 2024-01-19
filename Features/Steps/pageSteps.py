from datetime import datetime
from behave import when, then
from Helpers.requestsHelper import get_saved_response, get_page_response
from Helpers.searchHelper import get_page_key


@when('The page details for "{page_title}" are requested')
def request_page_details_of_title(context, page_title):
    search_response = get_saved_response()
    key = get_page_key(search_response["pages"], page_title)
    context.response = get_page_response(key)

@then('It has a latest timestamp > "{given_timestamp}"')
def compare_timestamp(context, given_timestamp):
    page_timestamp = context.response["latest"]["timestamp"]
    timestamp_datetime = datetime.strptime(page_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    given_timestamp_datetime = datetime.strptime(given_timestamp, "%Y-%m-%d")
    assert timestamp_datetime > given_timestamp_datetime, f"Timestamp is not greater than {given_timestamp}"
