# coding: utf-8
import json
import logging
import requests


logger = logging.getLogger(__name__)


class Client(object):
    def get(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return json.loads(response.content)

        raise Exception('HTTP ERROR {0}'.format(response.status_code))

    def post(self, url, payload):
        response = requests.post(url, payload)

        if response.status_code == 201:
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}'.format(response.status_code))

    def put(self, url):
        return NotImplementedError()

    def delete(self, url):
        response = requests.delete(url)

        if response.status_code in (200, 202, 204):
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}'.format(response.status_code))
