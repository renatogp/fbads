# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.customaudience import CustomAudienceResource


class CustomAudienceManager(Manager):
    resource_class = CustomAudienceResource
    resource_name = 'customaudiences'

    def _delete_api_path(self, object_id):
        return '{0}'.format(object_id)

    def add(self, name, description=None, opt_out_link=None):
        payload = {
            'name': name,
            'description': description,
            'opt_out_link': opt_out_link,
        }

        content = super(CustomAudienceManager, self).add(
            payload=payload
        )

        return content['id']
