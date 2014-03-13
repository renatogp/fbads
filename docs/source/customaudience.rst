================
Custom audiences
================


.. note::
    Before using the Custom Audiences API you must `accept the Terms of Service`_.

.. _`accept the terms of service`: https://www.facebook.com/ads/manage/customaudiences/tos.php


Creating a custom audience
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.customaudience.add(name, description=None, opt_out_link=None)

   Add a new custom audience to the ad account

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

Adding users
^^^^^^^^^^^^

.. py:function:: fbads.customaudience.add_users(customaudience_id, facebook_ids=[], emails=[])

   You can add users using facebook_ids or e-mails. ``fbads`` will hash the e-mail list using md5.

   :param str customaudience_id: Custom audience ID
   :param str facebook_ids: List of Facebook IDs
   :param str emails: List of emails -- do not hash the email list, it will be done automatically

   :rtype: ``True`` (hopefully!)


Exemplo: ::

    from fbads import FBAds

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    api.customaudience.add_users(
        customaudience_id='12345678987654321',
        emails=[
            'example-01@email.com',
            'example-02@email.com',
            'example-03@email.com',
            # ...
        ],
    )

    # you cannot use emails and facebook_ids at the same time, so
    api.customaudience.add_users(
        customaudience_id='12345678987654321',
        facebook_ids=[
            '12345678987001',
            '12345678987002',
            '12345678987003',
            # ...
        ],
    )


----


Removing a custom audience
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.customaudience.delete(customaudience_id)

   Removes a custom audience from the ad account

   :param str customaudience_id: Custom audience ID
   :rtype: True


Exemplo: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    api.customaudience.delete('123456787654321')

