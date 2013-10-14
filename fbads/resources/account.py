# coding: utf-8
from fbads.resources.base import Resource


class AccountStatus(object):
    ACTIVE = 1
    DISABLED = 2
    UNSETTLED = 3
    PENDING_REVIEW = 7
    PENDING_CLOSURE = 100
    UNAVAILABLE = 101

    choices = (
        (ACTIVE, u'Active'),
        (DISABLED, u'Disabled'),
        (UNSETTLED, u'Unsettled'),
        (PENDING_REVIEW, u'Pending review'),
        (UNAVAILABLE, u'Unavailable'),
        (PENDING_CLOSURE, u'Pending closure'),
    )


class AccountResource(Resource):
    pass
