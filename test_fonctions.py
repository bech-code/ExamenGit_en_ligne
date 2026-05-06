import unittest
from mesfonctions import addition, soustraction, multiplication, division, est_pair

class TestFonctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(0, 5), -5)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(0, 100), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5.0)
        with self.assertRaises(ValueError):
            division(5, 0)

    def test_est_pair(self):
        self.assertTrue(est_pair(4))
        self.assertFalse(est_pair(7))
        self.assertTrue(est_pair(0))

if __name__ == '__main__':
    unittest.main()
