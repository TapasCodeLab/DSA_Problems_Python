from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        room = [0]*n
        current_time = 0
        available_rooms, available_meetings = [], []
        for start, end in meetings:
            heapq.heappush(available_meetings,[start, end-start])
        for i in range(n):
            heapq.heappush(available_rooms, i)

        ongoing_meetings = []
        while available_meetings:
            start, duration = heapq.heappop(available_meetings)
            while ongoing_meetings and ongoing_meetings[0][0]<=start:
                end_time, room_no = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room_no)

            if available_rooms:
                room_no = heapq.heappop(available_rooms)
                current_time = max(current_time,start)
                heapq.heappush(ongoing_meetings,[current_time+duration, room_no])
                room[room_no] += 1
                continue
            else:
                lowest_end_time = ongoing_meetings[0][0]
                while ongoing_meetings and ongoing_meetings[0][0] <= lowest_end_time:
                    end_time, room_no = heapq.heappop(ongoing_meetings)
                    heapq.heappush(available_rooms, room_no)

                room_no = heapq.heappop(available_rooms)
                current_time = max(current_time, lowest_end_time)
                heapq.heappush(ongoing_meetings, [current_time + duration, room_no])
                room[room_no] += 1

        _max_number_meetings = max(room)
        for i in range(n):
            if room[i]==_max_number_meetings:
                return i



import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(self.sol.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]),0)

    def testcase2(self):
        self.assertEqual(self.sol.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]),1)

    def testcase3(self):
        self.assertEqual(self.sol.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8],[5,20],[7,10],[8,5],[9,9],[10,8]]),2)

    def testcase4(self):
        self.assertEqual(self.sol.mostBooked(n = 3, meetings = [[0,10],[1,5],[2,7],[3,4]]),1)

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()
