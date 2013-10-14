# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.user import UserResource


class UserManager(Manager):
    resource_class = UserResource
    resource_name = 'aduser'

    def add(self, uid, role):
        return super(UserManager, self).add(
            payload={
                'uid': uid,
                'role': role,
            }
        )

    def delete(self, uid):
        return super(UserManager, self).delete(object_id=uid)
