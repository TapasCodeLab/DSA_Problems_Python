# https://www.geeksforgeeks.org/problems/meeting-rooms-iii/1

class Solution:
    def mostBooked(self, n, meetings):
        # code here
        import heapq
        meeting_rooms = [0] * n
        available = [i for i in range(n)]
        heapq.heapify(available)
        busy = []
        meetings.sort(key=lambda x: x[0])

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                meeting_rooms[room] += 1
                heapq.heappush(busy, [end, room])
            else:
                time, room = heapq.heappop(busy)
                meeting_rooms[room] += 1
                heapq.heappush(busy, [time + end - start, room])

        return meeting_rooms.index(max(meeting_rooms))


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.mostBooked(n = 2, meetings = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]),1)

    def testcase2(self):
        self.assertEqual(self.solution.mostBooked(n = 4, meetings = [[0, 8], [1, 4], [3, 4], [2, 3]]),2)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()

