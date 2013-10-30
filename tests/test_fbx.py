# coding: utf-8
from mock import patch
from fbads import FBAds
from tests import BaseTestCase


class FBAdsFBXTestCase(BaseTestCase):
    def test_add(self):
        with patch('requests.post') as mocked_requests:
            mocked_requests.return_value.status_code = 201
            mocked_requests.return_value.content = ''

            fbads = FBAds(account_id=123456789)
            fbads.fbx.add(
                name=u'Group name',
                campaign_id=34285239857623,
                creative={
                    'title': u'Procurando algo?',
                    'body': u'Você só encontra algo aqui!',
                    'image_url': u'https://tekpix.com/tekpix.jpg',
                },
            )

    def test_add_url(self):
        fbads = FBAds(account_id=123456789)

        self.assertEqual(
            fbads.fbx._get_full_url(
                fbads.fbx._add_api_path(), {'access_token': 'abc'}
            ),
            'https://graph.facebook.com/act_123456789/adgroups?access_token=abc',
        )
