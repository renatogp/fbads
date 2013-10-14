# coding: utf-8
from fbads.resources.base import Resource


class CampaignStatus(object):
    ACTIVE = 1
    PAUSED = 2

    choices = (
        (ACTIVE, u'Active'),
        (PAUSED, u'Paused'),
    )


class CampaignResource(Resource):
    datetime_fields = ['start_time', 'end_time', 'updated_time', 'created_time']
    cents_to_decimal = ['daily_budget', 'lifetime_budget']
