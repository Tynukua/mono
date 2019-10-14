from requests import get

HEADERS = {
    'Request Content-Types': 'application/json',
    'Response Content-Types': 'application/json', 
    'Schemes': 'https', 
    'Version': '201906' }
    
BASE_URL = 'https://api.monobank.ua'

class OpenMono:
    def __init__(self, token, version = None):
        self._TOKEN = token
        #if version:
            #HEADERS['Version'] = str(version)
    
    def client_info(self):
        response = get(BASE_URL+'/personal/client-info', 
            headers = {**HEADERS, **{'X-Token': self._TOKEN} })
        return response.json()
