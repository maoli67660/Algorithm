import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_val_index = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        notInSet = val not in self.map_val_index
        if notInSet:
            self.list.append(val)
            self.map_val_index[val] = len(self.list) - 1

        return notInSet

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        result = val in self.map_val_index
        if result:
            index = self.map_val_index[val]
            if index == len(self.list) - 1:
                self.list.pop()
            else:
                tail = self.list.pop()
                self.list[index] = tail
                self.map_val_index[tail] = index

            del self.map_val_index[val]

        return result

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.list) == 0:
            return None
        randInt = random.randint(0, len(self.list) - 1)
        return self.list[randInt]


# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]


# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[1],[2],[2],[],[1],[2],[]]


# ["RandomizedSet","insert","insert","getRandom","getRandom","insert","remove","getRandom","getRandom","insert","remove"]
# [[],[3],[3],[],[],[1],[3],[],[],[0],[0]]
if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(3))
    print(obj.insert(3))

    print(obj.getRandom())
    print(obj.getRandom())

    print(obj.insert(1))
    print(obj.remove(3))

    print(obj.getRandom())
    print(obj.getRandom())

    print(obj.insert(0))

    print(obj.map_val_index)
    print(obj.list)

    print(obj.remove(0))
