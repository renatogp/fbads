# coding: utf-8
from datetime import datetime
from dateutil.tz import tzoffset
from decimal import Decimal
from fbads import FBAds
from tests import BaseTestCase


class FBAdsSetTestCase(BaseTestCase):

    def test_get_adset(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            adset = fbads.set.get('6016248730082', fields=['name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget'])
            self.assertEqual(adset.id, '6016248730082')
            self.assertEqual(adset.name, 'Test campaign')
            self.assertEqual(adset.start_time, datetime(2014, 5, 1, 0, 0, 0, tzinfo=tzoffset(None, -25200)))
            self.assertEqual(adset.end_time, datetime(2014, 5, 5, 0, 0, tzinfo=tzoffset(None, -25200)))
            self.assertEqual(adset.lifetime_budget, Decimal('10.00'))

    def test_add_set(self):
        from fbads.resources.set import SetStatus

        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            set_id = fbads.set.add(
                name=u'Test campaign',
                campaign_group_id='6016248662482',
                campaign_status=SetStatus.ACTIVE,
                lifetime_budget=Decimal('10.00'),
                start_time=datetime(2014, 5, 1, 0, 0, 0),
                end_time=datetime(2014, 5, 5, 0, 0, 0),
            )

            self.assertEqual(set_id, '6016248730082')

    def test_list_sets(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            sets = fbads.set.list(fields=['name'], limit=10)
            self.assertEqual(len(sets), 1)

            adset = sets.pop()
            self.assertEqual(adset.name, u'Test campaign')
            self.assertEqual(adset.id, '6016248730082')

    def test_delete_set(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token=self.get_test_access_token())
            deleted = fbads.set.delete('6016248730082')
            self.assertTrue(deleted)
