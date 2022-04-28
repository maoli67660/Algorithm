# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 10 天  哈希表
* 剑指 Offer II 030. 插入、删除和随机访问都是 O(1) 的容器 (设计,数组,哈希表,数学,随机化,中等,通过率 54.7%)
```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls = []
        self.dict = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.ls)
            self.ls.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        
        idx = self.dict[val]
        self.ls[idx] = self.ls[-1]
        self.dict[self.ls[idx]] = idx
        self.ls.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.ls)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

* 剑指 Offer II 031. 最近最少使用缓存 (设计,哈希表,链表,双向链表,中等,通过率 53.9%)
> 使用 OrderedDict 的 move_to_end(key)方法

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
            return 

        if self.size == self.capacity:
            self.od.popitem(0)
        else:
            self.size+=1
        self.od[key] = value

            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
* 剑指 Offer II 032. 有效的变位词 (哈希表,字符串,排序,简单,通过率 60.3%)
```python
Counter(s) == Counter(t) and t!=s
```
