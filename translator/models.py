from django.db import models
from django.conf import settings
from collections.abc import Mapping

import requests as r2
import json

class translate(models.Model):
    URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
    KEY = 'MTY2ZTcxNTQtZWQ1OC00NWI4LWI0MGEtNDg4ZDNkYmRjZTk0OjJjYjVmODM4ZTBlMDRjNmE5NGVhMjMzYTE1ZGYxNzJl'
    word = models.TextField()
    res = models.TextField()
    def translats(self):
        headers_auth = {'Authorization': 'Basic ' + self.KEY}
        auth = r2.post(self.URL_AUTH, headers= headers_auth)
        if auth.status_code == 200:
            token = auth.text     
            self.word = input('')
            if self.word:
                headers_translate = {
                    'Authorization': 'Bearer ' + token
                }
                params = {
                    'text': self.word,
                    'srcLang': 1033,
                    'dstLang': 1049
                }
                r = r2.get(self.URL_TRANSLATE, headers = headers_translate, params = params)
                self.res = r.json()
                try:
                    return(self.res["Translation"]["Translation"])
                except:
                    return('Not found translation')
        else:
            return('Error!')
    