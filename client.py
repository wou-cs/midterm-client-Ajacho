import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    url = "http://chrisbrooks.pythonanywhere.com/api/programmers"
    response = requests.get(url)
    data = response.json()
    # Json data is a dictionary
    return len(data["programmers"])
    

def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    url = f"http://chrisbrooks.pythonanywhere.com/api/programmers/{pid}"
    response = requests.get(url)
    programmerbyid = response.json()

    if response.status_code == 404:
        return {}

    if not programmerbyid:
        return {}

    if not isinstance(programmerbyid, dict):
        return {}
    return programmerbyid


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """

    url = "http://chrisbrooks.pythonanywhere.com/api/programmers/by_first_name/{first_name}"
    url = url.replace("{first_name}", first_name)
    data = requests.get(url)
    data = data.json()
    programmers = data["programmers"]
    if not programmers:
        return None
    if isinstance(programmers, list):
        for programmer in programmers:
            if programmer["first"].lower() == first_name.lower():
                return f"{programmer['first']} {programmer['last']}"
    return None




