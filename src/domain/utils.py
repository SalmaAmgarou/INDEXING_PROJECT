def get_dictionary_key(dictionary):
    if dictionary is not None:
        for key, element in dictionary.items():
            return key
    return None


def get_dictionary_element(dictionary):
    if dictionary is not None:
        for key, element in dictionary.items():
            return element
    return None
