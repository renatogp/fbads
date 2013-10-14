# coding: utf-8
import json
import unittest
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds


class FBAdsCampaignTestCase(unittest.TestCase):
    # def test_list_campaigns(self):
    #     fbads = FBAds(account_id=123456789)
    #     self.assertRaises(NotImplementedError, fbads.account.list)

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


    # def test_add_campaign(self):
    #     fbads = FBAds(account_id=123456789)
    #     self.assertRaises(NotImplementedError, fbads.account.add, 'some data')

    # def test_delete_campaign(self):
    #     fbads = FBAds(account_id=123456789)
    #     self.assertRaises(NotImplementedError, fbads.account.delete, 123456789)
