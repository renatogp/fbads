# coding: utf-8
import json
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCustomAudienceTestCase(BaseTestCase):
    def test_add_custom_audience(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            customaudience_id = fbads.customaudience.add(
                name=u'Test CA',
                description=u'All test users',
            )

            self.assertEqual(customaudience_id, '6015403089082')

    def test_add_users_to_custom_audience_facebook_ids(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            added = fbads.customaudience.add_users(
                customaudience_id='6015403089082',
                facebook_ids=[
                    '12345678987654321',
                    '12345678987654322',
                    '12345678987654323',
                ]
            )
            self.assertTrue(added)

    def test_add_users_to_custom_audience_emails(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            added = fbads.customaudience.add_users(
                customaudience_id='6015403089082',
                emails=[
                    'email1@email.com',
                    'email2@email.com',
                ]
            )
            self.assertTrue(added)

    def test_add_users_to_custom_audience_assertion_error(self):
        # you should not pass emails and facebook_ids at the same time
        fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')

        self.assertRaises(
            AssertionError,
            fbads.customaudience.add_users,
            customaudience_id='6015403089082',
            emails=[
                'email1@email.com',
                'email2@email.com',
            ],
            facebook_ids=[
                '12345678987654321',
                '12345678987654322',
                '12345678987654323',
            ]
        )

    def test_delete_custom_audience(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            deleted = fbads.customaudience.delete('6015403089082')

            self.assertTrue(deleted)

    def test_removing_users_to_custom_audience_emails(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            deleted = fbads.customaudience.delete_users(
                customaudience_id='6015403089082',
                emails=[
                    'email1@email.com',
                    'email2@email.com',
                ]
            )
            self.assertTrue(deleted)
