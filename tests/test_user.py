# coding: utf-8
import json
import unittest
from mock import patch
from fbads import FBAds


class FBAdsUserTestCase(unittest.TestCase):
    def test_list_users(self):
        with patch('requests.get') as mocked_requests:
            mocked_requests.return_value.status_code = 200
            mocked_requests.return_value.content = json.dumps({
                "data": [{
                    "id": 121211,
                    "permissions": [
                        1, 2, 3, 4, 5, 7
                    ],
                    "role": 1001
                }]
            })

            ads = FBAds()
            users = ads.user.list()
            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].id, 121211)
            self.assertEqual(users[0].role, 1001)
            self.assertEqual(users[0].permissions, [1, 2, 3, 4, 5, 7])

    def test_add_user(self):
        from fbads.resources.user import Role

        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 201
            mocked_requests.return_value.content = ''

            ads = FBAds()
            ads.user.add(
                uid='121211',
                role=Role.ADMIN,
            )
            # no exceptions... ok!?

    def test_delete_user(self):
        with patch('requests.delete') as mocked_requests:
            mocked_requests.return_value.status_code = 204
            mocked_requests.return_value.content = ''

            ads = FBAds()
            ads.user.delete('121211')
            # no exceptions... ok!?
