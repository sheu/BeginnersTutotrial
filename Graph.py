import cv2
import numpy as np
import time

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 10000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])

    return best_node


def dijkstra(G, v):
    dist_so_far = {v: 0}
    final_dist = {}
    path_so_far = {v: []}
    final_path = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        final_dist[w] = dist_so_far[w]
        final_path[w] = path_so_far[w]
        del dist_so_far[w]
        del path_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    path_so_far[x] = final_path[w] + [x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    path_so_far[x] = final_path[w] + [x]
    return final_dist, final_path


def make_link(G, a, b, weight):
    if a not in G:
        G[a] = {}
    G[a][b] = weight

    if b not in G:
        G[b] = {}
    G[b][a] = weight


def mid_point(pt1, pt2):
    return tuple((int((pt2[0] + pt1[0])/2), int((pt2[1] + pt1[1])/2)))


def draw_graph(in_g, in_coord):
    for node in in_g:
        cv2.circle(img, in_coord[node], 4, (255, 255, 255), -1, 0)
        cv2.putText(img, node, in_coord[node], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        for neighbour in G[node]:
            cv2.line(img, in_coord[node], in_coord[neighbour], (0, 255, 0), 8, cv2.LINE_AA)
            cv2.putText(img, str(in_g[node][neighbour]), mid_point(in_coord[node], in_coord[neighbour]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            cv2.imshow('Graph', img)


def draw_path(in_coord, in_path, start_node):
    start = start_node
    for end in in_path:
        cv2.line(img, in_coord[start], in_coord[end], (125, 125, 125), 3, cv2.LINE_AA)
        start = end
        cv2.imshow('Graph', img)



G = {}
(a, b, c, d, e, f, g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
tripples = ((a, c, 3), (c, b, 10), (a, b, 15), (d, b, 9), (a, d, 4), (d, f, 7), (d, e, 3), (e, g, 1), (e, f, 1), (f, g, 2), (b, f, 1))
coord = {a: (474, 146), b: (26, 137), c: (268, 55), d: (380, 316), e: (256, 500), f: (80, 239), g: (97, 447)}
for (i, j, k) in tripples:
    make_link(G, i, j, k)

final_dist, final_path = dijkstra(G, f)
print(final_dist)
print(final_path)
print(G)
img = np.zeros((600, 900, 3), np.uint8)
cv2.imshow('Graph', img)
draw_graph(G, coord)
draw_path(coord, final_path[a], f)

cv2.waitKey(0)
cv2.destroyAllWindows()





