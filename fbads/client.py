# coding: utf-8
import json
import logging
import requests


logger = logging.getLogger(__name__)


class Client(object):
    def get(self, url):
        response = requests.get(url)

        logger.info(u'GET {0} - Response HTTP {1}: {2}'.format(url, response.status_code, response.content))

        if response.status_code == 200:
            return json.loads(response.content)

        raise Exception('HTTP ERROR {0}: {1}'.format(response.status_code, response.content))

    def post(self, url, payload):
        # payload = json.dumps(payload)

        response = requests.post(url, payload)

        logger.info(u'POST {0}, {1} - Response: {2}'.format(url, payload, response.content))

        if response.status_code in (200, 201):  # it shouldn't return 200 but...
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}: {1}'.format(response.status_code, response.content))

    def put(self, url):
        return NotImplementedError()

    def delete(self, url):
        response = requests.delete(url)

        logger.info(u'DELETE {0} - Response HTTP {1}: {2}'.format(url, response.status_code, response.content))

        if response.status_code in (200, 202, 204):
            return json.loads(response.content) if response.content else None

        raise Exception('HTTP ERROR {0}: {1}'.format(response.status_code, response.content))
