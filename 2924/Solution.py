def findChampion(n, edges):
        indeg = [0] * n
        for _, v in edges:
            indeg[v] += 1
        return -1 if indeg.count(0) != 1 else indeg.index(0)
n = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
print(findChampion(n, edges))
