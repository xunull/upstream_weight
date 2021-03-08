import unittest

from upstream_weight import (
    Traffic,
    TrafficItem,
    tune_upstream_ratio,
    tune_upstream_weight,
)


class MyTestCase(unittest.TestCase):
    def test_tune_upstream_weight(self):
        a = Traffic.parse_obj({
            "aws": TrafficItem(ratio=73, count=7),
            "ali": TrafficItem(ratio=27, count=6),
            "ten": TrafficItem(ratio=0, count=10)
        })
        b = tune_upstream_weight(a)
        self.assertEqual(b.aws.weight, 146)
        self.assertEqual(b.ali.weight, 63)
        self.assertEqual(b.ten.weight, 0)

    def test_tune_upstream_ratio(self):
        a = Traffic.parse_obj({
            "aws": TrafficItem(weight=146, count=7),
            "ali": TrafficItem(weight=63, count=6),
            "ten": TrafficItem(weight=0, count=10)
        })
        b = tune_upstream_ratio(a)
        self.assertEqual(b.aws.ratio, 73)
        self.assertEqual(b.ali.ratio, 27)


if __name__ == '__main__':
    unittest.main()
