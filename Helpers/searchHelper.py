def check_value_in_attribute(pages, attribute, value):
    for page in pages:
        if page[attribute] == value:
            return True
    return False
