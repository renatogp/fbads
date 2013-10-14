# coding: utf-8
import json
import logging
import requests


logger = logging.getLogger(__name__)


class Client(object):
    def get(self, url):
        response = requests.get(url)

        logger.info(u'GET {0}'.format(url))

        if response.status_code == 200:
            return json.loads(response.content)

        raise Exception('HTTP ERROR {0}'.format(response.status_code))

    def post(self, url, payload):
        payload = json.dumps(payload)

        response = requests.post(url, payload)

        logger.info(u'POST {0}, {1}'.format(url, payload))

        if response.status_code == 201:
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}'.format(response.status_code))

    def put(self, url):
        return NotImplementedError()

    def delete(self, url):
        response = requests.delete(url)

        logger.info(u'DELETE {0}'.format(url))

        if response.status_code in (200, 202, 204):
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}'.format(response.status_code))
