import unittest

from garden import bed_summary, days_to_harvest, water_litres


class TestGarden(unittest.TestCase):
    def test_days_to_harvest(self):
        self.assertEqual(days_to_harvest("lettuce", 45), 0)
        self.assertEqual(days_to_harvest("tomato", 30), 50)

    def test_water_litres(self):
        self.assertEqual(water_litres({"tomato": 4, "lettuce": 10}), 11.0)

    def test_bed_summary(self):
        self.assertEqual(
            bed_summary({"bean": 6}, 55), ["bean: 0 days to harvest"]
        )


if __name__ == "__main__":
    unittest.main()
