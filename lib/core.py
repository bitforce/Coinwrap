#! /usr/local/bin/python2

import requests


_session = None


def __init__(self, url='https://api.coinmarketcap.com/v1/', timeout=120):
    self.timeout = timeout
    self.url = url


def session(self):
    if not self._session:
        self._session = requests.Session()
        self._session.headers.update({'Content-Type': 'application/json'})
        self._session.headers.update({'User-agent': 'coinmarketcap - python wrapper\
                                      around coinmarketcap.com (github.com/mrsmn/\
                                      coinmarketcap-api)'})
        return self._session


def __request(self, endpoint, params):
    response = self.session.get(self.url + endpoint, params=params, timeout=self.timeout)
    if response.status_code != 200:
        raise Exception('error connecting to endpoint')
    try:
        response = response.json()
    except ValueError:
        raise Exception('could not parse response as JSON')


def ticker(self, currency="", **kwargs):  # A.?
    params = {}
    params.update(kwargs)
    return self.__request('ticker/' + currency, params)


def data(self, **kwargs):
    params = {}
    params.update(kwargs)
    return self.__request('global/', params)
