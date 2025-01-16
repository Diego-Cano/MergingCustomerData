import unittest
from merge_logic import merge

class TestMergeFunction(unittest.TestCase):
    def test_normal_cases(self):
        #Test1
        customerData1 = [1, 2, 3, 0, 0, 0]
        merge(customerData1, 3, [4, 5, 6], 3)
        self.assertEqual(customerData1, [1, 2, 3, 4, 5, 6])

        #Test2
        customerData1 = [5, 10, 15, 0, 0, 0]
        merge(customerData1, 3, [20, 25, 30], 3)
        self.assertEqual(customerData1, [5, 10, 15, 20, 25, 30])

        #Test3
        customerData1 = [1, 2, 0, 0]
        merge(customerData1, 2, [5, 6], 2)
        self.assertEqual(customerData1, [1, 2, 5, 6])