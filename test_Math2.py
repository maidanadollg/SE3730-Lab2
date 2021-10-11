import unittest
import Math2

class Test_test_Math2(unittest.TestCase):
    def test_sum(self):
        from Math2 import sum
        a= sum(1, 2)
        self.assertEqual(a, 3)

if __name__ == '__main__':
    unittest.main()
    
