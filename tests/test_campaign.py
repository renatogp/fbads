# coding: utf-8
from datetime import datetime
from dateutil.tz import tzoffset
from decimal import Decimal
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCampaignTestCase(BaseTestCase):
    def test_get_campaign(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            campaign = fbads.campaign.get('6015348517682', fields=['name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget'])
            self.assertEqual(campaign.id, '6015348517682')
            self.assertEqual(campaign.name, 'Test campaign')
            self.assertEqual(campaign.start_time, datetime(2014, 3, 11, 7, 31, 5, tzinfo=tzoffset(None, -25200)))
            self.assertEqual(campaign.end_time, datetime(2014, 12, 1, 0, 0, tzinfo=tzoffset(None, -28800)))
            self.assertEqual(campaign.lifetime_budget, Decimal('500.00'))

    def test_add_campaign(self):
        from fbads.resources.campaign import CampaignStatus

        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            campaign_id = fbads.campaign.add(
                name=u'Test campaign',
                campaign_status=CampaignStatus.ACTIVE,
                lifetime_budget=Decimal('500.00'),
                start_time=datetime(2013, 6, 1, 0, 0, 0),
                end_time=datetime(2014, 12, 1, 0, 0, 0),
            )

            self.assertEqual(campaign_id, '6015348798482')

    def test_list_campaigns(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            campaigns = fbads.campaign.list(fields=['name'], limit=10)
            self.assertEqual(len(campaigns), 1)

            campaign = campaigns.pop()
            self.assertEqual(campaign.name, u'Test campaign')
            self.assertEqual(campaign.id, '6015348517682')

    def test_delete_campaign(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            deleted = fbads.campaign.delete('6015348798482')
            self.assertTrue(deleted)
