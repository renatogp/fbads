# coding: utf-8
import json
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCampaignTestCase(BaseTestCase):
    def test_get_campaign(self):
        with patch('requests.get') as mocked_requests:
            mocked_requests.return_value.status_code = 200
            mocked_requests.return_value.content = json.dumps({
                'id': 2345234523453,
                'name': 'Campaign name',
                'campaign_status': 1,
                'start_time': '2013-01-01T12:00:00',
                'end_time': '2013-12-01T12:00:00',
                'daily_budget': 1234,
                'lifetime_budget': 12345
            })

            fbads = FBAds(account_id=123456789)
            campaign = fbads.campaign.get(2345234523453)
            self.assertEqual(campaign.id, 2345234523453)
            self.assertEqual(campaign.name, 'Campaign name')
            self.assertEqual(campaign.start_time, datetime(2013, 01, 01, 12, 00, 00))
            self.assertEqual(campaign.end_time, datetime(2013, 12, 01, 12, 00, 00))
            self.assertEqual(campaign.daily_budget, Decimal('12.34'))
            self.assertEqual(campaign.lifetime_budget, Decimal('123.45'))

    def test_add_campaign(self):
        from fbads.resources.campaign import CampaignStatus

        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 201
            mocked_requests.return_value.content = '{"id": 12345678987654321}'

            fbads = FBAds(account_id=123456789)
            fbads.campaign.add(
                name=u'Test campaign',
                campaign_status=CampaignStatus.ACTIVE,
                daily_budget=Decimal('1.50'),
                lifetime_budget=Decimal('5.00'),
                start_time=datetime(2013, 6, 1, 0, 0, 0),
                end_time=datetime(2014, 6, 1, 0, 0, 0),
            )

    def test_delete_campaign(self):
        with patch('requests.delete') as mocked_requests:
            mocked_requests.return_value.status_code = 204
            mocked_requests.return_value.content = ''

            fbads = FBAds(account_id=123456789)
            fbads.campaign.delete(121211)
            # no exceptions... ok!?
