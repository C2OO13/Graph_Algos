import numpy as np
import queue


def explore_neighbours(p, q, x, y, m, visited, nodes_next):
    neighbour_x = [-1, +1, 0, 0]
    neighbour_y = [0, 0, -1, +1]
    for i in range(0, 4):
        x1 = p + neighbour_x[i]
        y1 = q + neighbour_y[i]
        if x1 < 0 or y1 < 0: continue
        if x1 > 4 or y1 > 6: continue
        if visited[x1][y1] == 1: continue
        if m[x1][y1] == -1: continue
        x.put(x1)
        y.put(y1)
        visited[x1][y1] = 1
        nodes_next = nodes_next + 1
    return x, y, visited, nodes_next


def solve(start_x, start_y, end_x, end_y, m):
    x = queue.Queue(maxsize=0)
    y = queue.Queue(maxsize=0)
    x.put(start_x)
    y.put(start_y)
    cnt = 0
    found = False
    visited = np.zeros((5, 7))
    visited[start_x][start_y] = 1
    nodes_next, nodes_current = 0, 1
    while not x.empty():
        p = x.get()
        q = y.get()
        if p == end_x and q == end_y:
            found = True
            break
        x, y, visited, nodes_next = explore_neighbours(p, q, x, y, m, visited, nodes_next)
        nodes_current = nodes_current - 1
        if nodes_current == 0:
            nodes_current = nodes_next
            nodes_next = 0
            cnt = cnt + 1
    if found:
        return cnt
    return -1


if __name__ == "__main__":
    m = [
        [0, 0, 0, -1, 0, 0, 0],
        [0, -1, 0, 0, 0, -1, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, 0],
        [-1, 0, -1, 0, 0, -1, 0]
    ]
    start_x, start_y = 0, 0
    end_x, end_y = 4, 3
    cnt = solve(start_x, start_y, end_x, end_y, m)
    print("Steps = {0}".format(cnt))
