# coding: utf-8
import json
from datetime import datetime
from decimal import Decimal
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsGroupTestCase(BaseTestCase):
    def test_add_group(self):
        from fbads.resources.group import BidInfo, BidType, TargetingSpecs

        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')

            targeting_specs = TargetingSpecs()
            targeting_specs.add_custom_audience('6014532845282', '205084400_abandoned_cart')

            group_id = fbads.group.add(
                name=u'Ad group name',
                bid_type=BidType.CPC,
                bid_info=BidInfo.get(
                    BidType.CPC,
                    clicks=Decimal('0.25'),
                ),
                campaign_id='6015348517682',
                creative_id='6014479876682',
                targeting_specs=targeting_specs,
            )
            self.assertEqual(group_id, '6015415795282')

    def test_list_groups(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            groups = fbads.group.list(fields=['name', 'bid_info'], limit=10)
            self.assertEqual(len(groups), 1)

            group = groups.pop()
            self.assertEqual(group.name, u'Ad group name')

            #TODO: should we convert this back to Decimal('0.25')?
            self.assertEqual(group.bid_info['CLICKS'], 25)

    def test_delete_group(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            deleted = fbads.group.delete('6015415795282')
            self.assertTrue(deleted)
