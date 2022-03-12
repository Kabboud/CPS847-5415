import unittest
from math import cps5415

class TestSampleMethods(unittest.TestCase):
      def test_cps5415(self):
        """
        Test cps5415 function
        """
        self.assertEqual(cps5415(7), 42)
        
if __name__ == '__main__':
    unittest.main()
