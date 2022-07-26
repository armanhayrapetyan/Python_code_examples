#Selection sort
a = [-3, 5, 0, -8, 1, 10]
N = len(a)

for i in range(N-1):
    m = a[i]
    p = i
    for j in range(i+1, N):
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:
      a[i],a[p] = a[p],a[i]

#print(a)

# Insertion sort
a = [-3, 5, 0, -8, 1, 10]
N = len(a)

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

#print(a)

# Bubble sort

a = [7, 5, -8, 0, 10, 1]
N = len(a)

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

#print(a)

# Quck sort

import random

def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)

    return a


a = [9, 5, -3, 4, 7, 8, -8]
a = quick_sort(a)

print(a)



# Merge sort
def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


a = [9, 5, -3, 4, 7, 8, -8]
a = split_and_merge_list(a)

#print(a)







