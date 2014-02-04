# coding: utf-8
import json
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCustomAudienceTestCase(BaseTestCase):
    def test_add_custom_audience(self):
        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 200
            mocked_requests.return_value.content = '{"id": 12345678987654321}'

            fbads = FBAds(account_id=123456789)
            customaudience_id = fbads.customaudience.add(
                name=u'Test CA',
                description=u'All test users',
            )

        self.assertTrue(customaudience_id)

    def test_delete_campaign(self):
        with patch('requests.delete') as mocked_requests:
            mocked_requests.return_value.status_code = 204
            mocked_requests.return_value.content = ''

            fbads = FBAds(account_id=123456789)
            deleted = fbads.customaudience.delete(12345678987654321)

        self.assertTrue(deleted)
