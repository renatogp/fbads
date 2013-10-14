# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.user import UserResource


class UserManager(Manager):
    resource_class = UserResource
    resource_name = 'aduser'

    def add(self, user_id, role):
        return super(UserManager, self).add(
            payload={
                'uid': user_id,
                'role': role,
            }
        )

    def delete(self, user_id):
        return super(UserManager, self).delete(object_id=user_id)
