=========
Ad groups
=========

Create an ad group
^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.group.add(name, bid_type, bid_info, campaign_id, creative_id, targeting_specs)

   Add a new ad group to the ad account

   :param str name: Ad group name
   :param BidType bid_type: ``BidType.CPC``, ``BidType.CPM``, ``BidType.MULTI_PREMIUM``, ``BidType.ABSOLUTE_OCPM``, ``BidType.CPA`` (from ``fbads.resources.group.BidType``)
   :param BidInfo bid_info: bid - must be an BidInfo (``fbads.resources.group.BidInfo``) instance (see the examples below)
   :param str set_id: Ad set ID
   :param str creative_id: Creative ID
   :param TargetingSpecs targeting_specs: a TargetingSpecs (``fbads.resources.group.TargetingSpecs``) instances - see the examples below

   :rtype: An ad group ID (str)

.. note::
    There a few other attributes (tracking_specs, conversion_specs, view_tags) not mentioned here -- take a look at ``fbads/managers/group.py`` if you need to use them


Example: ::

    from decimal import Decimal
    from fbads import FBAds
    from fbads.resources.group import BidInfo, BidType, TargetingSpecs

    fbads = FBAds(account_id='1234', access_token='a_valid_token')

    targeting_specs = TargetingSpecs()

    # target to one (or many) custom audiences
    targeting_specs.add_custom_audience('a_custom_aud_id', 'a_custom_aud_name')
    targeting_specs.add_custom_audience('a_custom_aud_id', 'a_custom_aud_name')

    # you can exclude a specific custom audience
    targeting_specs.exclude_custom_audience('a_custom_aud_id', 'a_custom_aud_name')

    # and / or filter by age
    targeting_specs.age_min = 18
    targeting_specs.age_max = 35

    # you *always* need to specify at least one country
    # this is the only required targeting attribute
    targeting_specs.countries = ['BR', 'US']

    group_id = fbads.group.add(
        name=u'An ad group name',
        bid_type=BidType.CPC,
        bid_info=BidInfo.get(
            BidType.CPC,
            clicks=Decimal('0.25'),
        ),
        campaign_id='an_ad_campaign_id',
        creative_id='an_ad_creative_id',
        targeting_specs=targeting_specs,
    )

    print u'Created ad group with ID {0}'.format(group_id)

----


List ad groups
^^^^^^^^^^^^^^

.. py:function:: fbads.group.list([fields, limit])

   List all ad groups.

   :param list fields: Fields to be retrieved
   :param int limit: An optional limit

   :rtype: list of GroupResource


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    for group in api.group.list(fields=['name', 'bid_info'], limit=10):
        print u'{0}: bid is {1}'.format(group.name, group.bid_info)


----


Remove an ad group
^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.group.delete(group_id)

   Remove an ad group from the ad account

   :param str group_id: Group ID
   :rtype: True


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    print api.group.delete('14352345234523')  # returns True
