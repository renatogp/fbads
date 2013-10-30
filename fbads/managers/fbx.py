# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.fbx import FBXResource
from fbads.resources.group import BidType


class FBXManager(Manager):
    resource_class = FBXResource
    resource_name = 'adgroups'

    def _add_api_path(self):
        return 'act_{0}/{1}'.format(self._api.account_id, self.resource_name)

    def add(self, name, campaign_id, creative):
        assert set(creative.keys()) == set(['title', 'body', 'image_url']), u'You must provide "title",  "body" and "image_url" args'

        creative.update({
            # FBX works only with CPC
            'bid_type': BidType.CPC,
        })

        payload = {
            'name': name,
            'campaign_id': campaign_id,
            'creative': creative,
        }

        return super(FBXManager, self).add(
            payload=payload
        )
