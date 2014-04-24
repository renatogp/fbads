# coding: utf-8
from fbads.resources.base import Resource


class SetStatus(object):
    ACTIVE = 'ACTIVE'
    PAUSED = 'PAUSED'

    choices = (
        (ACTIVE, u'Active'),
        (PAUSED, u'Paused'),
    )


class SetResource(Resource):
    datetime_fields = ['start_time', 'end_time', 'updated_time', 'created_time']
    cents_to_decimal = ['daily_budget', 'lifetime_budget']
