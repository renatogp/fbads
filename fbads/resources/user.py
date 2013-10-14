# coding: utf-8
from fbads.resources.base import Resource


class Role(object):
    ADMIN, MANAGER, REPORTS = 1001, 1002, 1003

    choices = (
        (ADMIN, u'Administrator'),
        (MANAGER, u'Ad manager'),
        (REPORTS, u'Reports only'),
    )


class Permission(object):
    ACCOUNT_ADMIN = 1
    ADMANAGER_READ, ADMANAGER_WRITE = 2, 3
    BILLING_READ, BILLING_WRITE = 4, 5
    REPORTS = 7

    choices = (
        (ACCOUNT_ADMIN, u'Can modify the set of users associated with the given account'),
        (ADMANAGER_READ, u'Can view campaigns and ads'),
        (ADMANAGER_WRITE, u'Can manage campaigns and ads'),
        (BILLING_READ, u'Can view account billing information'),
        (BILLING_WRITE, u'Can modify the account billing information'),
        (REPORTS, u'Can run reports'),
    )


class UserResource(Resource):
    pass
