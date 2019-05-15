import requests

from time import sleep


BTC_URL = 'https://chain.api.btc.com/v3/'

sleep_time = .25


def call_api(resource, payload=None):
    """
    Build URL and Make an API request
    :param str resource: url endpoint being called
    :return: json api response
    """
    url = BTC_URL + resource
    if payload:
        response = requests.get(url, params=payload)
    else:
        response = requests.get(url)
    if response.status_code == 403:  # try waiting
        sleep(sleep_time)
        if payload:
            response = requests.get(url, params=payload)
        else:
            response = requests.get(url)
    return handle_response(response)


def handle_response(response):
    """
    Correct the response datatype if returned incorrectly
    :response Requests.models.Response: a response from the api
    :return: response ready for consumption from wrapper
    """
    print
    data = response.json()
    if data['err_no'] == 0:
        return data['data']
    else:
        print(data['err_msg'])
        return data['err_msg']