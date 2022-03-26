from queue import PriorityQueue


class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return 0
        pq = PriorityQueue()
        pq.put((intervals[0][1], intervals[0]))
        intervals.pop(0)
        max_room_num = 1
        while intervals:
            cur_meeting = intervals.pop(0)
            q_top = pq.queue[0][1]
            if not q_top[1] > cur_meeting[0]:
                pq.get()
            pq.put((cur_meeting[1], cur_meeting))

            if max_room_num < pq.qsize():
                max_room_num = pq.qsize()
        return max_room_num


if __name__ == '__main__':
    solution = Solution()
    result = solution.minMeetingRooms([[13, 15], [1, 13]])
    print("result = ", result)
