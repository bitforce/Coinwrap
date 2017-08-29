import requests


def ticker(self, currency="", **kwargs):  # A.?
    params = {}
    params.update(kwargs)
    return self.request('ticker/' + currency, params)


def data(self, **kwargs):
    params = {}
    params.update(kwargs)
    return self.request('global/', params)
