# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.group import GroupResource, BidType


class GroupManager(Manager):
    resource_class = GroupResource
    resource_name = 'adgroup'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def add(self, name, bid_type, bid_info, campaign_id, creative_id, targeting_specs, tracking_specs=None, conversion_specs=None, view_tags=[], redownload=False):
        assert not redownload  # if redownload is True, must instantiate a resource_class object... later

        if bid_type in (BidType.ABSOLUTE_OCPM, BidType.CPA):
            assert conversion_specs, u'provide arg conversion_specs'

        payload = {
            'name': name,
            'bid_type': bid_type,
            'campaign_id': campaign_id,
            'creative': {
                'creative_id': creative_id,
            },
            'targeting_specs': targeting_specs.get(),
        }

        if tracking_specs:
            payload.update({
                'tracking_specs': tracking_specs.get(),
            })

        if conversion_specs:
            payload.update({
                'conversion_specs': conversion_specs,
            })

        if view_tags:
            payload.update({
                'view_tags': view_tags,
            })

        return super(GroupManager, self).add(
            payload=payload
        )
