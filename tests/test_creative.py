# coding: utf-8
from fbads import FBAds
from tests import BaseTestCase


class FBAdsCreativeTestCase(BaseTestCase):

    def test_add_creative(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            creative_id = fbads.creative.add(
                title=u'Test creative',
                body=u'Testing creative creation! Lorem ipsum here.',
                link_url='http://fbads.readthedocs.org/en/latest/index.html',
                image_url='https://d1dhh18vvfes41.cloudfront.net/417x300/051057500.jpg',
            )

            self.assertEqual(creative_id, '6015403647082')

    def test_list_creatives(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            creatives = fbads.creative.list(fields=['title'], limit=10)
            self.assertEqual(len(creatives), 1)

            creative = creatives.pop()
            self.assertEqual(creative.id, '6014479876682')
            self.assertEqual(creative.title, 'Luizalabs.com')

    def test_delete_creative(self):
        with self.replay():
            fbads = FBAds(account_id='1378857852381224', access_token='a_valid_token')
            deleted = fbads.creative.delete('6015403647082')

            self.assertTrue(deleted)
