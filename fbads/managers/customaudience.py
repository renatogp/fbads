# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.customaudience import CustomAudienceResource


class CustomAudienceManager(Manager):
    resource_class = CustomAudienceResource
    resource_name = 'customaudiences'

    def add(self, name, description=None, opt_out_link=None):
        payload = {
            'name': name,
            'description': description,
            'opt_out_link': opt_out_link,
        }

        return super(CustomAudienceManager, self).add(
            payload=payload
        )
