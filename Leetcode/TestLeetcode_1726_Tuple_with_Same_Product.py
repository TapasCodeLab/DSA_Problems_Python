from Leetcode.Leetcode_1726_Tuple_with_Same_Product import Solution
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_tupleSameProduct_1(self):
        self.assertEqual(self.solution.tupleSameProduct([2,3,4,6]),8)

    def test_tupleSameProduct_2(self):
        self.assertEqual(self.solution.tupleSameProduct([1,2,4,5,10]), 16)

    def test_tupleSameProduct_3(self):
        self.assertEqual(self.solution.tupleSameProduct([2,4,8,16,32,64,128,256,512,1024,2048,4096]), 760)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()