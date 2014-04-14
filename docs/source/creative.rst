============
Ad creatives
============

Create an ad creative
^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.creative.add(title, body, object_url, image_url, actor_id=None)

   Add a new creative to the ad account

   :param str name: Creative title
   :param str body: Body (ad text)
   :param str object_url: Target URL
   :param str image_url: Ad image URL
   :param str actor_id: An optional Facebook Object ID (eg.: a page)


   :rtype: An ad creative ID (str)


Example: ::

    from fbads import FBAds

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    creative_id = fbads.creative.add(
        title=u'Test creative',
        body=u'Testing creative creation! Lorem ipsum here.',
        object_url='http://fbads.readthedocs.org/en/latest/index.html',
        image_url='https://d1dhh18vvfes41.cloudfront.net/417x300/051057500.jpg',
    )

    print u'Creative created with ID {0}'.format(creative_id)


----


List creatives
^^^^^^^^^^^^^^

.. py:function:: fbads.creative.list([fields, limit])

   List all ad creatives.

   :param list fields: Fields to be retrieved
   :param int limit: An optional limit
   :rtype: list of CreativeResource


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    for creative in api.creative.list(fields=['title'], limit=10):
        print creative.title


----


Remove an ad creative
^^^^^^^^^^^^^^^^^^^^^

.. py:function:: fbads.creative.delete(creative_id)

   Removes an ad creative from the ad account

   :param str creative_id: Creative ID
   :rtype: True


Example: ::

    api = FBAds(
        account_id='1233',
        access_token='token_with_ads_permission',
    )

    print api.creative.delete('123456787654321')  # returns True
