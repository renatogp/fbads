# coding: utf-8
from fbads import FBAds
from tests import BaseTestCase


class FBAdsAccountTestCase(BaseTestCase):
    def test_list_accounts(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.list)

    def test_get_account(self):
        with self.replay():
            fbads = FBAds(account_id='1374333772780983', access_token='a_valid_token')
            account = fbads.account.get('1374333772780983', fields=['id', 'name'])
            self.assertEqual(account.id, 'act_1374333772780983')
            self.assertEqual(account.account_id, '1374333772780983')

    def test_add_account(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.add, 'some data')

    def test_delete_account(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.delete, 123456789)
