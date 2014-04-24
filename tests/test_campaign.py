# coding: utf-8
from datetime import datetime
from dateutil.tz import tzoffset
from decimal import Decimal
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCampaignTestCase(BaseTestCase):

    def test_get_campaign(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            campaign = fbads.campaign.get('6016248666482', fields=['name'])
            self.assertEqual(campaign.id, '6016248666482')
            self.assertEqual(campaign.name, 'Test campaign')

    def test_add_campaign(self):
        from fbads.resources.campaign import CampaignStatus

        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            campaign_id = fbads.campaign.add(
                name=u'Test campaign',
                campaign_group_status=CampaignStatus.ACTIVE,
            )

            self.assertEqual(campaign_id, '6016248666482')

    def test_list_campaigns(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            campaigns = fbads.campaign.list(fields=['name'], limit=10)
            self.assertEqual(len(campaigns), 2)

            campaign = campaigns.pop()
            self.assertEqual(campaign.name, u'Test campaign')
            self.assertEqual(campaign.id, '6016248666482')

    def test_delete_campaign(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            deleted = fbads.campaign.delete('6016248666482')
            self.assertTrue(deleted)
