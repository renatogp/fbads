================
Custom audiences
================


.. note::
    Before using the Custom Audiences API you must `accept the Terms of Service`_.

.. _`accept the terms of service`: https://www.facebook.com/ads/manage/customaudiences/tos.php


Creating a custom audience
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.customaudience.add(name, description=None, opt_out_link=None)

   Add a new campaign to the ad account

   :param str name: Custom audience name
   :param str description: Custom audience description
   :param str opt_out_link: Custom audience description

   :rtype: A custom audience ID (long)


Exemplo: ::

    from fbads import FBAds

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    custom_audience_id = api.customaudience.add(
        name=u'Test custom audience',
        description='My custom audience',
    )

    print u'Custom audience created with ID {0}'.format(custom_audience_id)


----


Removing a custom audience
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.customaudience.delete(customaudience_id)

   Remove custom audience from the ad account

   :param str customaudience_id: Custom audience ID
   :rtype: True


Exemplo: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    api.customaudience.delete('123456787654321')

