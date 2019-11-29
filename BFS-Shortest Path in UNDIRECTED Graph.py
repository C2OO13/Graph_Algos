import numpy as np
import queue


def solve(start, n, g):
    q = queue.Queue(maxsize=0)
    visited = np.zeros(n)
    prev = []
    for i in range(0, n):
        prev.append(-1)
    # print(prev)
    q.put(start)
    visited[start] = 1
    while not q.empty():
        node = q.get()
        for x in range(0, n):
            if g[node][x] == 0:
                continue
            if visited[x] == 0:
                q.put(x)
                # print(x)
                visited[x] = 1
                prev[x] = node
                # print(prev[0])
    # print(prev)
    return prev


def reconstruct(start, end, prev):
    path = []
    x = end
    while x != -1:
        path.append(x)
        x = prev[x]
    path.reverse()
    if path[0] == start:
        return path
    return []


def bfs(start, end, n, g):
    prev = solve(start, n, g)
    return reconstruct(start, end, prev)


def main():
    n = 13
    g = [[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]
    start = 5
    end = 12
    path = bfs(start, end, n, g)
    print(path)


if __name__ == '__main__':
    main()
