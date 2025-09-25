from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UF()


class UF:
    def __init__(self):
        self._container = dict()
        self._size = dict()

    def find(self, x: int) -> int:
        if x not in self._container:
            self._container[x] = x
            self._size[x] = 1

        return self._container[x]

    def union(self, x: int, y: int) -> int:

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return self._size[x_root]

        self._container[y_root] = x_root
        self._size[x_root] += self._size[y_root]

        return self._size[x_root]
