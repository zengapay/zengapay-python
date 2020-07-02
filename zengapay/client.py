"""
Base Implementation of the ZengaPay API client

@author: Patrick Walukagga
"""


import json
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


import requests
from requests import Request, Session
from requests.auth import AuthBase

from .config import ZengaPayConfig


class Response:

    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers
        self.data = body


class ZengaPayAuth(AuthBase):
    """Attaches Authentation to the given Requesst Object."""

    def __init__(self, token):
        self.token = token
    
    def __call__(self, req):
        # Modify and return the request

        req.headers["Authorization"] = f"Bearer {self.token}"
        return req


class ClientInterface():
    def get_auth_token(self):
        raise NotImplementedError

    def get_transaction_status(self):
        return NotImplementedError


class Client(ClientInterface):
    def get_auth_token(self):
        return super(Client, self).get_auth_token()
    
    def get_transaction_status(self):
        return super(Client, self).get_transaction_status()


class ZengaPayAPI(ClientInterface):

    def __init__(self, config, **kwargs):
        super(ZengaPayAPI, self).__init__(**kwargs)
        self._session = Session()
        self._config = ZengaPayConfig(config)
    
    @property
    def config(self):
        return self._config
