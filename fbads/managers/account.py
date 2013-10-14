# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.account import AccountResource


class AccountManager(Manager):
    resource_class = AccountResource
    resource_name = 'adaccount'

    def list(self, *args, **kwargs):
        raise NotImplementedError()

    def get(self, object_id, fields=['id', 'name', 'status']):
        return super(AccountManager, self).get(object_id=object_id, fields=fields)

    def add(self, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, *args, **kwargs):
        raise NotImplementedError()
