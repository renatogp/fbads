# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.user import UserResource


class UserManager(Manager):
    resource_class = UserResource
    resource_name = 'user'
