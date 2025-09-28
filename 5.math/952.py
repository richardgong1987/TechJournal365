from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return self.size[ra]
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def build_spf(limit):
    spf = list(range(limit + 1))
    for i in range(2, int(limit ** 0.5) + 1):
        if spf[i] == i:
            step = i
            for x in range(i * i, limit + 1, step):
                if spf[x] == x:
                    spf[x] = i
    return spf


def factor_distinct_primes(x, spf):
    ps = set()
    while x > 1:
        p = spf[x]
        ps.add(p)
        while x % p == 0:
            x //= p
    return ps


class Solution:
    def largestComponentSize(self, nums):
        n = len(nums)
        if n <= 1: return n
        maxA = max(nums)
        spf = build_spf(maxA)

        dsu = DSU(n)
        first_idx = {}  # prime -> first index seen

        for i, val in enumerate(nums):
            for p in factor_distinct_primes(val, spf):
                if p in first_idx:
                    dsu.union(i, first_idx[p])
                else:
                    first_idx[p] = i

        # Count sizes per root
        count = defaultdict(int)
        best = 0
        for i in range(n):
            r = dsu.find(i)
            count[r] += 1
            if count[r] > best:
                best = count[r]
        return best
