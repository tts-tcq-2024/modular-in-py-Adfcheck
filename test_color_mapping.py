import unittest
from color_mapping import get_color_from_pair_number, get_pair_number_from_color

class TestColorMapping(unittest.TestCase):
    def test_number_to_pair(self):
        self.assertEqual(get_color_from_pair_number(4), ('White', 'Brown'))
        self.assertEqual(get_color_from_pair_number(5), ('White', 'Slate'))

    def test_pair_to_number(self):
        self.assertEqual(get_pair_number_from_color('Black', 'Orange'), 12)
        self.assertEqual(get_pair_number_from_color('Violet', 'Slate'), 25)
        self.assertEqual(get_pair_number_from_color('Red', 'Orange'), 7)

if __name__ == '__main__':
    unittest.main()
