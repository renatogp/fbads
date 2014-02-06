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

        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 201
            mocked_requests.return_value.content = ''

            fbads = FBAds(account_id=123456789)

            targeting_specs = TargetingSpecs()
            targeting_specs.add_custom_audience(id=5424653456345, name='ml_id_290009')

            fbads.group.add(
                name=u'Group name',
                bid_type=BidType.CPC,
                bid_info=BidInfo.get(
                    BidType.CPC,
                    clicks=Decimal('0.25'),
                ),
                campaign_id=4523452345234523,
                creative_id=4523452345234,
                targeting_specs=targeting_specs,
            )

    def test_delete_group(self):
        with patch('requests.delete') as mocked_requests:
            mocked_requests.return_value.status_code = 204
            mocked_requests.return_value.content = ''

            fbads = FBAds(account_id=123456789)
            fbads.group.delete(3456345634565)
