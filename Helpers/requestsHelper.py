import requests

from Utilities.TestBase import TestBase

search_endpoint_url = f"{TestBase.BaseUrl}{TestBase.ApiVersion}/wikipedia/{TestBase.Languages[0]}{TestBase.SEARCH_ENDPOINT}"
page_endpoint_url = f"{TestBase.BaseUrl}{TestBase.ApiVersion}/wikipedia/{TestBase.Languages[0]}{TestBase.PAGE_ENDPOINT}"

saved_response = None


def get_search_response(search_string):
    params = {"q": search_string, "limit": TestBase.SearchLimitMax}
    response = requests.get(search_endpoint_url, params=params)
    return response.json()


def get_page_response(page_key):
    response = requests.get(f"{page_endpoint_url}/{page_key}/bare")
    return response.json()


def save_response(response):
    global saved_response
    saved_response = response


def get_saved_response():
    return saved_response
