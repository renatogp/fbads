# coding: utf-8
import logging
import os
import unittest
from httreplay import replay as with_replay, filter_query_params_key, filter_headers_key


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG)

    def _test_name_for_replay_file(self):
        """
        Stolen from https://github.com/davepeck/httreplay#slightly-more-advanced-usage
        """
        return self.__str__().split(' ')[0]

    def _replay_file_name(self):
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'recorded',
                self.__class__.__name__,
                "{0}.json".format(self._test_name_for_replay_file())
            )
        )

    def replay(self):
        return with_replay(
            self._replay_file_name(),
            url_key=filter_query_params_key(['access_token']),
            headers_key=filter_headers_key(['User-Agent']),
        )
