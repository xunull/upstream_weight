import unittest

from upstream_weight import (
    Traffic,
    TrafficItem,
    tune_upstream_ratio,
    tune_upstream_weight,
)


class MyTestCase(unittest.TestCase):

    def test_tune_upstream_weight(self):
        # ratio to weight
        a = Traffic.parse_obj({
            "aaa": TrafficItem(ratio=73, count=7),
            "bbb": TrafficItem(ratio=27, count=6),
            "ccc": TrafficItem(ratio=0, count=10)
        })
        b = tune_upstream_weight(a)
        self.assertEqual(b.aaa.weight, 146)
        self.assertEqual(b.bbb.weight, 63)
        self.assertEqual(b.ccc.weight, 0)

    def test_tune_upstream_ratio(self):
        # weight to ratio
        a = Traffic.parse_obj({
            "aaa": TrafficItem(weight=146, count=7),
            "bbb": TrafficItem(weight=63, count=6),
            "ccc": TrafficItem(weight=0, count=10)
        })
        b = tune_upstream_ratio(a)
        self.assertEqual(b.aaa.ratio, 73)
        self.assertEqual(b.bbb.ratio, 27)


if __name__ == '__main__':
    unittest.main()
