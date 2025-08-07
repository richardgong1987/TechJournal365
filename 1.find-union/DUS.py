class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        # Initialize if x is unseen
        if x not in self.parent:
            self.parent[x] = x
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return  # already in the same set

        self.parent[rootY]  = rootX


uf = UnionFind()
uf.union("apple", "banana")
uf.union("banana", "cherry")

print(uf.find("apple"))    # Same root as cherry
print(uf.find("cherry"))   # Same root


class Node:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Node({self.name})"
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name

a = Node("A")
b = Node("B")
c = Node("C")

uf = UnionFind()
uf.union(a, b)
uf.union(b, c)

print(uf.find(a))  # should be same as find(c)
print(uf.find(c))