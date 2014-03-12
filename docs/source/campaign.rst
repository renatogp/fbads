============
Ad campaigns
============

Create an ad campaign
^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.campaign.add(name, campaign_status, daily_budget=None, lifetime_budget=None, start_time=None, end_time=None)

   Add a new campaign to the ad account

   :param str name: Campaign name
   :param str campaign_status: ``CampaignStatus.ACTIVE`` or ``CampaignStatus.INACTIVE`` (from ``fbads.resources.campaign.CampaignStatus``)
   :param Decimal daily_budget: Daily budget for this campaign, use ``Decimal``
   :param Decimal lifetime_budget: Lifetime budget for this campaign, use ``Decimal``
   :param datetime start_time: The campaign start date
   :param datetime end_time: The campaign End date

   :rtype: An ad campaign ID (str)


Example: ::

    from decimal import Decimal
    from fbads import FBAds
    from fbads.resources.campaign import CampaignStatus

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    campaign_id = api.campaign.add(
        name=u'Testing campaign #001',
        campaign_status=CampaignStatus.ACTIVE,
        daily_budget=Decimal('1.00'),
    )

    print u'Campaign created with ID {0}'.format(campaign_id)

----


List campaigns
^^^^^^^^^^^^^^

.. py:function:: fbads.campaign.list([limit])

   List all account campaigns.

   :param int limit: An optional limit
   :rtype: list of CampaignResource


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    for campaign in api.campaign.list(fields=['name'], limit=10):
        print campaign.name


----


Remove an ad campaign
^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.campaign.delete(campaign_id)

   Remove an ad campaign from the ad account

   :param long campaign_id: Campaign ID
   :rtype: True


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    print api.campaign.delete(123456787654321)  # returns True
