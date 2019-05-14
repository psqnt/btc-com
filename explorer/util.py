import requests


BASE_URL = 'https://chain.api.btc.com/v3/'


def call_api(resource):
    """
    Build URL and Make an API request
    :param str resource: url endpoint being called
    :return: json api response
    """
    url = BASE_URL + resource
    try:
        response = requests.get(url).json()
    except Exception as e:
        print(e)
        response = e
    return response


def handle_response(response):
    """
    Correct the response datatype if returned incorrectly
    :response Requests.models.Response: a response from the api
    :return: response ready for consumption from wrapper
    """
    if isinstance(response, dict):
        print(response)
        return response
    else:
        return response