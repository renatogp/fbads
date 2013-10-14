# coding: utf-8
from fbads.client import Client
from fbads.managers.user import UserManager


class FBAds(object):
    def __init__(self, account_id, access_token=None):
        self.account_id = account_id
        self.access_token = access_token
        self.client = Client()

    @property
    def user(self):
        return UserManager(self)
