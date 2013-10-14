# coding: utf-8


class Manager(object):
    resource_class = None
    resource_name = None

    def __init__(self, api):
        self._api = api

    def list(self, url=None):
        response = self._api.client.get(url)
        return [self._dict_to_resource(r) for r in response['data']]

    def get(self, url=None):
        response = self._api.client.get(url)
        return self._dict_to_resource(response)

    def add(self, payload, url=None):
        return self._api.client.post(url, payload)

    def delete(self, object_id=None, url=None):
        return self._api.client.delete(url)

    def _dict_to_resource(self, data, resource_class=None, fields=[], exclude=[]):
        """
        Convert a dict to a `resource_class` instance
        """
        return (resource_class or self.resource_class)(
            self,
            data,
            fields=fields,
            exclude=exclude,
        )
