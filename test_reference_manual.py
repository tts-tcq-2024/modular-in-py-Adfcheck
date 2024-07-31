import unittest
from reference_manual import generate_reference_manual

class TestReferenceManual(unittest.TestCase):
    def test_generate_reference_manual(self):
        manual = generate_reference_manual()
        self.assertIn('Pair Number 1: White Blue', manual)
        self.assertIn('Pair Number 25: Violet Slate', manual)
        self.assertEqual(len(manual.split('\n')), 25)  # Ensure there are 25 pairs

if __name__ == '__main__':
    unittest.main()
