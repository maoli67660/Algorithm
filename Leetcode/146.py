class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_dict = {}
        self.point_dict = {}
        self.q_head = Node(-1)
        self.q_tail = self.q_head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            self._move_to_end(key)
            return self.lru_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update
        if key in self.lru_dict:
            self._move_to_end(key)
        # insert
        else:
            # LRU are not full
            if self.capacity > self.size:
                self.size = self.size + 1
            else:
                top_key = self._pop_top()
                del self.lru_dict[top_key]
                del self.point_dict[top_key]

            point = self._insert_at_end(key)
            self.point_dict[key] = point

        self.lru_dict[key] = value

    def _pop_top(self):
        top = self.q_head.next
        self.q_head.next = top.next
        if self.q_head.next is not None:
            self.q_head.next.previous = self.q_head
        #print('pop: ', top.data)
        return top.data

    def _insert_at_end(self, key):
        node = Node(key)
        node.previous = self.q_tail
        self.q_tail.next = node
        self.q_tail = node
        return node

    def _move_to_end(self, key):
        point = self.point_dict[key]
        if point == self.q_tail:
            return

        point.previous.next = point.next
        point.next.previous = point.previous

        point.previous = self.q_tail
        self.q_tail.next = point
        self.q_tail = point


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(capacity=1)
cache.put(2, 1)
print(cache.get(2))
cache.put(3, 2)

print(cache.get(3))

