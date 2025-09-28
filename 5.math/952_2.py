from typing import List


class UF:
    def __init__(self, n):
        self._parent = list(range(n))
        self._size = [1] * n

    def find(self, x: int) -> int:
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def get_size(self, x: int) -> int:
        return self._size[self.find(x)]

    def union(self, a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return
        if self._size[a_root] < self._size[b_root]:
            a_root, b_root = b_root, a_root

        self._parent[b_root] = a_root
        self._size[a_root] += self._size[b_root]


def build_SPF(num: int) -> List[int]:
    spf = list(range(num + 1))

    for n in range(2, int(num ** 0.5) + 1):
        if spf[n] == n:
            for n2 in range(n * n, n + 1, n):
                if spf[n2] == n2:
                    spf[n2] = n

    return spf


def factor_distinct_primes(num: int, spf: List[int]) -> set[int]:
    ps = set()

    while num > 1:
        p = spf[num]
        ps.add(p)

        while num % p == 0:
            num = num // p

    return ps


class Solution:
    def largestComponentSize(self, nums):
        n = len(nums)
        if n <= 1: return n

        uf = UF(n)
        max_num = max(nums)
        SPF = build_SPF(max_num)

        first_seen = {}

        for i, val in enumerate(nums):
            for p in factor_distinct_primes(val, SPF):
                if p in first_seen:
                    uf.union(i, first_seen[p])
                else:
                    first_seen[p] = i

        max_len = 1
        for i in range(n):
            max_len = max(max_len, uf.get_size(i))
        return max_len


print(Solution().largestComponentSize([4, 6, 15, 35]))