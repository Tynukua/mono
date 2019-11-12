from requests import get
from .types import *
    
BASE_URL = 'https://api.monobank.ua'

class OpenMono:
    HEADERS = {
        'Request Content-Types': 'application/json',
        'Response Content-Types': 'application/json', 
        'Schemes': 'https', 
        'Version': '201906' }

    def __init__(self, token, version = None):
        self._TOKEN = token
        if version:
            OpenMono.HEADERS['Version'] = str(version)

    @property
    def __headers(self):
        return {**OpenMono.HEADERS, **{'X-Token': self._TOKEN}}

    def client_info(self):
        response = get(BASE_URL+'/personal/client-info', 
            headers=self.__headers).json() 
        response['accounts'] = [ MonoCard(i) for i in response['accounts'] ] 
        return ClientInfo(response)

