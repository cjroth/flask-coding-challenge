from unittest import TestCase

import json
from lib import InMemoryDateStatCache, get_data_from_cache


class TestApp(TestCase):

    def test_future_end_date(self):
        cache = InMemoryDateStatCache()
        actual_result = get_data_from_cache(cache, '2018-12-05', '2018-12-07')
        expected_result = [
            {"btc_price":3961.49333333,"date":"2018-12-05","output_volume":2223959.72628,"unique_addresses":492964.0},
        ]
        assert len(actual_result) == len(expected_result)
        self.assertDictEqual(actual_result[0], expected_result[0])
