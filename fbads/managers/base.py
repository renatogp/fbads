# coding: utf-8
import urllib
GRAPH_API_URL = 'https://graph.facebook.com/'


class Manager(object):
    resource_class = None
    resource_name = None

    def __init__(self, api):
        self._api = api

    def _add_api_path(self):
        return 'act_{0}/{1}'.format(self._api.account_id, self.resource_name)

    def _list_api_path(self):
        return 'act_{0}/{1}'.format(self._api.account_id, self.resource_name)

    def _get_api_path(self, object_id):
        return 'act_{0}/{1}/{2}'.format(self._api.account_id, self.resource_name, object_id)

    def _delete_api_path(self, object_id):
        # usually get, update and delete URLs are the same
        return self._get_api_path(object_id)

    def _update_api_path(self, object_id):
        # usually get, update and delete URLs are the same
        return self._get_api_path(object_id)

    def _get_full_url(self, path, args):
        encoded_args = urllib.urlencode(args)

        url = '{0}{1}?{2}'.format(
            GRAPH_API_URL,
            path,
            encoded_args,
        )

        return url

    def list(self, fields=[], limit=None):
        url = '{0}{1}?access_token={2}'.format(
            GRAPH_API_URL,
            self._list_api_path(),
            self._api.access_token,
        )

        if fields:
            url += '&fields={0}'.format(','.join(fields))

        if limit:
            url += '&limit={0}'.format(limit)

        response = self._api.client.get(url)

        return [self._dict_to_resource(r) for r in response['data']]

    def get(self, object_id, fields=[]):
        url = '{0}{1}?access_token={2}'.format(
            GRAPH_API_URL,
            self._get_api_path(object_id),
            self._api.access_token,
        )

        if fields:
            url += '&fields={0}'.format(','.join(fields))

        response = self._api.client.get(url)
        return self._dict_to_resource(response)

    def update(self, object_id, payload):
        url = '{0}{1}?access_token={2}'.format(
            GRAPH_API_URL,
            self._update_api_path(object_id),
            self._api.access_token,
        )

        return self._api.client.post(url, payload)

    def add(self, payload, api_path=None):
        url = self._get_full_url(
            path=api_path or self._add_api_path(),
            args={
                'access_token': self._api.access_token,
            },
        )

        return self._api.client.post(url, payload)

    def delete(self, object_id, payload=None, api_path=None):
        args = {
            'access_token': self._api.access_token,
        }

        # there's no payload for DELETE requests, converting
        # to url params
        if payload:
            args.update(payload)

        url = self._get_full_url(
            path=api_path or self._delete_api_path(object_id),
            args=args,
        )

        self._api.client.delete(url)

        return True

    def _dict_to_resource(self, data, resource_class=None):
        """
        Convert a dict to a `resource_class` instance
        """
        return (resource_class or self.resource_class)(
            self,
            data,
        )
