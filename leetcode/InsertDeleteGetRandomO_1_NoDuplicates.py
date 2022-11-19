import random

# Solution to this: https://www.youtube.com/watch?v=46dZH7LDbf8
# Done blind without looking at the solutions
# This is the version that doesn't allow duplicates.

# Turns out this is the solution to this systems design problem: https://leetcode.com/problems/insert-delete-getrandom-o1/

class Solution:
    def __init__(self):
        self.values = list()
        self.indices = dict()

    def get_random(self) -> int:
        return random.choice(self.values)

    def insert(self, number:int) -> int:
        if number in self.indices:
            return -1

        self.values.append(number)
        self.indices[number] = len(self.values) - 1
        return number

    def remove(self, number: int) -> int:
        if number not in self.indices:
            return -1

        index = self.indices.pop(number)
        last_added_item = self.values[-1]
        self.values[index] = last_added_item
        self.indices[last_added_item] = index
        self.values[-1] = number
        return self.values.pop()

    def print(self) -> int:
        print(self.values)

sol = Solution()
sol.insert(4)
sol.insert(4)
sol.insert(10)
sol.insert(13)
sol.insert(1)
sol.insert(3)
sol.remove(3)
sol.print()

print(sol.get_random())
