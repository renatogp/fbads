# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.campaign import CampaignResource


class CampaignManager(Manager):
    resource_class = CampaignResource
    resource_name = 'adcampaign_groups'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def list(self, fields=['id', 'name'], **kwargs):
        return super(CampaignManager, self).list(fields=fields, **kwargs)

    def add(self, name, campaign_group_status):
        payload = {
            'name': name,
            'campaign_group_status': campaign_group_status,
        }

        return super(CampaignManager, self).add(
            payload=payload
        )['id']
