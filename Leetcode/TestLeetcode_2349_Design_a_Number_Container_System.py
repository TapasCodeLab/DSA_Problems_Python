import unittest
from Leetcode_2349_Design_a_Number_Container_System import NumberContainers

class TestNumberContainers(unittest.TestCase):
    def setUp(self):
        self.nc = NumberContainers();

    def testcase_1(self):
        res = []
        res.append(self.nc.find(10))
        self.nc.change(2,10)
        self.nc.change(1, 10)
        self.nc.change(3, 10)
        self.nc.change(5, 10)
        res.append(self.nc.find(10))
        self.nc.change(1, 20)
        res.append(self.nc.find(10))
        self.assertEqual([-1,1,2],res)

    def tearDown(self):
        del self.nc


if __name__=='__main__':
    unittest.main()

