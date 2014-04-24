# coding: utf-8
from fbads.resources.base import Resource


class CampaignStatus(object):
    ACTIVE = 'ACTIVE'
    PAUSED = 'PAUSED'

    choices = (
        (ACTIVE, u'Active'),
        (PAUSED, u'Paused'),
    )


class CampaignResource(Resource):
    pass
