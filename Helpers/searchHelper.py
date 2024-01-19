def check_value_in_attribute(pages, attribute, value):
    for page in pages:
        if page[attribute] == value:
            return True
    return False


def get_page_key(pages, title_text):
    key = ""
    for page in pages:
        if page["title"] == title_text:
            key = page["key"]
            break
    if not key:
        print(f"Key not found for{title_text}")
    return key


def check_search_string_in_page(pages, search_string):
    for page in pages:
        for key, value in page.items():
            if search_string in str(value):
                break
            return True
    return False
