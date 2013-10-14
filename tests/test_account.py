# coding: utf-8
import json
import unittest
from mock import patch
from fbads import FBAds


class FBAdsAccountTestCase(unittest.TestCase):
    def test_list_accounts(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.list)

    def test_get_account(self):
        with patch('requests.get') as mocked_requests:
            mocked_requests.return_value.status_code = 200
            mocked_requests.return_value.content = json.dumps({
                'id': 123456789,
                'name': 'Account name',
            })

            fbads = FBAds(account_id=123456789)
            account = fbads.account.get(123456789, fields=['id', 'name'])
            self.assertEqual(account.id, 123456789)
            self.assertEqual(account.name, 'Account name')

    def test_add_account(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.add, 'some data')

    def test_delete_account(self):
        fbads = FBAds(account_id=123456789)
        self.assertRaises(NotImplementedError, fbads.account.delete, 123456789)
