# coding: utf-8
from decimal import Decimal
from fbads.resources.base import Resource


class Gender(object):
    MALE = 1
    FEMALE = 2


class BidType(object):
    CPC = 'CPC'
    CPM = 'CPM'
    MULTI_PREMIUM = 'MULTI_PREMIUM'
    ABSOLUTE_OCPM = 'ABSOLUTE_OCPM'
    CPA = 'CPA'

    choices = (
        (CPC, u'CPC'),
        (CPM, u'CPM'),
        (MULTI_PREMIUM, u'Multi premium'),
        (ABSOLUTE_OCPM, u'Absolute oCPM'),
        (CPA, u'CPA'),
    )


class BidInfo(object):

    @classmethod
    def get(cls, bid_type, impressions=None, clicks=None, actions=None, reach=None, social=None):
        info = {}
        if bid_type == BidType.CPM:
            assert impressions, u'provide arg "impressions"'
            assert isinstance(impressions, Decimal), u'invalid type, use Decimal()'

            info.update({
                'IMPRESSIONS': int(impressions * 100),
            })

        elif bid_type == BidType.CPC:
            assert clicks, u'provide arg "clicks"'
            assert isinstance(clicks, Decimal), u'invalid type, use Decimal()'

            info.update({
                'CLICKS': int(clicks * 100),
            })

        elif bid_type == BidType.ABSOLUTE_OCPM:
            assert actions and reach and clicks and social, u'provide args "actions", "reach", "clicks" and "social"'
            assert isinstance(actions, Decimal) and isinstance(reach, Decimal) and isinstance(clicks, Decimal) \
                and isinstance(social, Decimal), u'invalid type, use Decimal()'

            info.update({
                'ACTIONS': int(actions * 100),
                'REACH': int(reach * 100),
                'CLICKS': int(clicks * 100),
                'SOCIAL': int(social * 100),
            })

        elif bid_type == BidType.CPA:
            assert actions, u'provide arg "actions"'

            info.update({
                'ACTIONS': int(actions * 100),
            })

        return info


class TargetingSpecs(object):
    custom_audiences = []
    excluded_custom_audiences = []
    countries = []
    age_min = None
    age_max = None
    genders = None

    def add_custom_audience(self, id, name):
        self.custom_audiences.append({'id': id, 'name': name})

    def exclude_custom_audience(self, id, name):
        self.excluded_custom_audiences.append({'id': id, 'name': name})

    def get(self):
        spec = {
            'geo_locations': {
                'countries': self.countries,
            }
        }

        for attr in ('custom_audiences', 'excluded_custom_audiences', 'age_min', 'age_max', 'genders'):
            val = getattr(self, attr)
            if val:
                spec.update({attr: val})

        return spec


class GroupResource(Resource):
    pass
