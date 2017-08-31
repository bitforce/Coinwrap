import requests


class Market(object):

    _session = None

    def __init__(self, url='https://api.coinmarketcap.com/v1/', timeout=120):
        self.url = url
        self.timeout = timeout

    @property
    def session(self):
        self._session = requests.Session()
        self._session.headers.update({'Content-Type': 'application/json'})
        self._session.headers.update({'User-agent': 'github:\
                                       bitforce/wrapper-py-coinmarketcap'})
        return self._session

    def __request(self, endpoint, params):
        response_object = self.session.get(self.url + endpoint, params=params,
                                           timeout=self.timeout)
        if response_object.status_code != 200:
            raise Exception('An error occurred, please try again.')
        try:
            response = response_object.json()
        except(ValueError):
            raise Exception('could not parse response as JSON')

        return response

    def coin(self, currency="", **kwargs):
            params = {}
            params.update(kwargs)
            response = self.__request('ticker/' + currency, params)
            return response

    def stats(self, **kwargs):
            params = {}
            params.update(kwargs)
            response = self.__request('global/', params)
            return response
