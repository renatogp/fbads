# coding: utf-8
from fbads.client import Client
from fbads.managers.user import UserManager


class FBAds(object):
    def __init__(self):
        self.client = Client()

    @property
    def user(self):
        return UserManager(self)
