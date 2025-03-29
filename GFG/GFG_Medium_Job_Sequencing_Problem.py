# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        import heapq
        minheap = []
        jobs = [[deadline[i], profit[i]] for i in range(len(deadline))]
        jobs.sort(key=lambda x: (x[0], -x[1]))
        # print(jobs)
        total_job, total_profit = 0, 0

        for job in jobs:
            if total_job < job[0]:
                heapq.heappush(minheap, job[1])
                total_profit += job[1]
                total_job += 1
            elif total_job == job[0] and minheap[0] < job[1]:
                prev = heapq.heappop(minheap)
                heapq.heappush(minheap, job[1])
                total_profit = total_profit + job[1] - prev
            # print([total_job, total_profit])

        return [total_job, total_profit]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.jobSequencing(deadline = [4, 1, 1, 1], profit = [20, 10, 40, 30]),[2, 60])

    def testcase2(self):
        self.assertEqual(self.solution.jobSequencing(deadline = [2, 1, 2, 1, 1], profit = [100, 19, 27, 25, 15]), [2, 127])

    def testcase3(self):
        self.assertEqual(self.solution.jobSequencing(deadline = [3, 1, 2, 2], profit = [50, 10, 20, 30]), [3, 100])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()