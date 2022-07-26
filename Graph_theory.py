# #Algorithm Deikstra
# import math
#
# def arg_min(T, S):
#     amin = -1
#     m = math.inf
#     for i, t in enumerate(T):
#         if t < m and i not in S:
#             m = t
#             amin = i
#
#     return amin
#
# D = ((0, 3, 1, 3, math.inf, math.inf),
#      (3, 0, 4, math.inf, math.inf, math.inf),
#      (1, 4, 0, math.inf, 7, 5),
#      (3, math.inf, math.inf, 0, math.inf, 2),
#      (math.inf, math.inf, 7, math.inf, 0, 4),
#      (math.inf, math.inf, 5, 2, 4, 0))
#
# N = len(D)
# T = [math.inf]*N
#
# v = 0
# S = {v}
# T[v] = 0
# M = [0]*N
#
# while v != -1:
#     for j, dw in enumerate(D[v]):
#         if j not in S:
#             w = T[v] + dw
#             if w < T[j]:
#                 T[j] = w
#                 M[j] = v
#
#     v = arg_min(T, S)
#     if v >= 0:
#         S.add(v)
#
# #print(T, M, sep="\n"
#
# start = 0
# end = 4
# P = [end]
# while end != start:
#     end = M[P[-1]]
#     P.append(end)
#
# print(P)
#
# # Algorithm floyda
#
# import math
#
#
# def get_path(P, u, v):
#     path = [u]
#     while u != v:
#         u = P[u][v]
#         path.append(u)
#
#     return path
#
#
# V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
#      [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
#      [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
#      [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
#      [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
# ]
#
# N = len(V)
# P = [[v for v in range(N)] for u in range(N)]
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             d = V[i][k] + V[k][j]
#             if V[i][j] > d:
#                 V[i][j] = d
#                 P[i][j] = k
#
#
# start = 1
# end = 4
# print(get_path(P, end, start))
#
#

# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
#
#    def insert(self, data):
#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          elif data > self.data:
#                if self.right is None:
#                   self.right = Node(data)
#                else:
#                   self.right.insert(data)
#       else:
#          self.data = data
#
#
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data),
#       if self.right:
#          self.right.PrintTree()
#
#
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()





















