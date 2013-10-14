# coding: utf-8
import logging
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG)
