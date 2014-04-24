# coding: utf-8
from fbads.client import Client
from fbads.managers.account import AccountManager
from fbads.managers.campaign import CampaignManager
from fbads.managers.customaudience import CustomAudienceManager
from fbads.managers.creative import CreativeManager
from fbads.managers.fbx import FBXManager
from fbads.managers.group import GroupManager
from fbads.managers.set import SetManager
from fbads.managers.user import UserManager


class FBAds(object):

    def __init__(self, account_id, access_token=None):
        self.account_id = account_id
        self.access_token = access_token
        self.client = Client()

    @property
    def account(self):
        return AccountManager(self)

    @property
    def campaign(self):
        return CampaignManager(self)

    @property
    def customaudience(self):
        return CustomAudienceManager(self)

    @property
    def creative(self):
        return CreativeManager(self)

    @property
    def fbx(self):
        return FBXManager(self)

    @property
    def group(self):
        return GroupManager(self)

    @property
    def user(self):
        return UserManager(self)

    @property
    def set(self):
        return SetManager(self)
