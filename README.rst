=====
fbads
=====

.. image:: https://api.travis-ci.org/rpedigoni/fbads.png
    :target: https://travis-ci.org/rpedigoni/fbads

Python client for the Facebook Ads API. Works with the new ads schema (ad sets). **Under development!**


Installation
------------

Install via ``pip``: ::

    $ pip install fbads


Usage
-----

Usage should be simple as: ::

    api = FBAds(account_id='123456789', access_token='a_valid_token')

    campaign_id = api.campaign.add(
        name=u'Testing campaign #001',
        campaign_status=CampaignStatus.ACTIVE,
    )

    print u'Campaign created with ID {0}'.format(campaign_id)


Docs
----
Documentation is available at http://fbads.readthedocs.org/en/latest/
