from queue import Queue


class Solution:

    def killProcess2(self, pid, ppid, kill):
        kids_map = {0:[]}
        for p in pid:
            kids_map[p] = []
        for index, p in enumerate(ppid):
            kids_map[p].append(pid[index])

        queue = Queue()
        queue.put(kill)
        result = []

        while not queue.empty():
            top = queue.get()
            result.append(top)
            for i in kids_map[top]:
                queue.put(i)
        return result

    def killProcess(self, pid, ppid, kill):
        queue = Queue()
        queue.put(kill)
        result = []
        while not queue.empty():
            process_2_kill = queue.get()
            result.append(process_2_kill)
            for index, x in enumerate(ppid):
                if x == process_2_kill:
                    queue.put(pid[index])
        return result


if __name__ == '__main__':
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    solution = Solution()

    print(solution.killProcess2(pid, ppid, 5))
