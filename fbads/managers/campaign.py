# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.campaign import CampaignResource


class CampaignManager(Manager):
    resource_class = CampaignResource
    resource_name = 'adcampaign'

    def list(self, fields=['id', 'name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget']):
        return super(CampaignManager, self).list(fields=fields)

    def add(self, name, campaign_status, daily_budget, lifetime_budget, start_time, end_time, redownload=False):
        assert not redownload  # if redownload is True, must instantiate a resource_class object... later

        return super(CampaignManager, self).add(
            payload={
                'name': name,
                'campaign_status': campaign_status,
                'daily_budget': daily_budget,
                'lifetime_budget': lifetime_budget,
                'start_time': start_time,
                'end_time': end_time,
                'redownload': redownload,
            }
        )

    def delete(self, uid):
        return super(CampaignManager, self).delete(object_id=uid)
