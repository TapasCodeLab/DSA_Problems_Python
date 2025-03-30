# https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1

class Solution:
    def startStation(self, gas, cost):
        # Your code here
        n = len(gas)
        available = [gas[i] - cost[i] for i in range(n)]
        available.extend(available)

        # Kadane's algorithm
        length, total = 0, 0
        for i in range(len(available)):
            total += available[i]
            if total < 0:
                total = 0
                length = 0
            else:
                length += 1
            if length == n:
                return i - n + 1
        return -1

        # # # Below code works but gives TLE
        # def isPossible(initial):
        #     available=0
        #     index = initial
        #     while True:
        #         available = available+gas[index]-cost[index]
        #         index = (index+1)%len(gas)
        #         if available<0:
        #             return False
        #         if index == initial:
        #             return True

        # for i in range(len(gas)):
        #     if gas[i]>=cost[i] and isPossible(i):
        #         return i

        # return -1


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.startStation(gas = [4, 5, 7, 4], cost= [6, 6, 3, 5]),2)

    def testcase2(self):
        self.assertEqual(self.solution.startStation(gas = [1, 2, 3, 4, 5], cost= [3, 4, 5, 1, 2]),3)

    def testcase3(self):
        self.assertEqual(self.solution.startStation(gas = [3, 9], cost = [7, 6]),-1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()