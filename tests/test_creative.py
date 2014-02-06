# coding: utf-8
import json
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCampaignTestCase(BaseTestCase):
    def test_add_creative(self):
        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 200
            mocked_requests.return_value.content = '{"id": 12345678987654321}'

            fbads = FBAds(account_id=123456789)
            creative_id = fbads.creative.add(
                title=u'Test creative',
                body=u'TEsting...',
                link_url='http://fbads.readthedocs.org/en/latest/index.html',
                image_url='https://d1dhh18vvfes41.cloudfront.net/417x300/051057500.jpg',
            )

            self.assertTrue(creative_id)

    # def test_delete_creative(self):
    #     with patch('requests.delete') as mocked_requests:
    #         mocked_requests.return_value.status_code = 204
    #         mocked_requests.return_value.content = ''

    #         fbads = FBAds(account_id=123456789)
    #         fbads.creative.delete(121211)
    #         # no exceptions... ok!?
