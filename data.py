data = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]


def Array2D(data,x = len(data)):
    t = x - 1
    for i in range(x):
        data[i][t],data[i][i] = data[i][i],data[i][t]
        t-=1
    return data


#print(Array2D(data))

from collections import Counter
data = [1, 2, 3, 6, 3, 6, 1,1,1,1,1,2,2,2,2,3,3,3,-4,-9,-7,-7]

lst = []
ls = Counter(data)
for k,v in ls.items():
    if v>=2:
        lst.append(k)
#print(lst)

#print(ls)


arr = [x for x in range(1,16)]

def binary_serch(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0

    while high >= low:
        mid  = (high+low) // 2
        if arr[mid] > x:
            high = mid-1

        elif arr[mid] < x:
            low = mid+1

        else:
            return f"Searchable number {arr[mid]} his index {mid}"

    return "Number not found"

a = binary_serch(arr,9)

print(a)


import time

def test_nod(func):
    a = 28
    b = 35
    res = func(a,b)
    if res ==7:
        print("#Test1-ok")
    else:
        print("#Test1-fail")

    a= 2
    b = 100
    res = func(a,b)
    if res ==2:
        print("#Test2-ok")
    else:
        print("#Test2-fail")

    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    rs = et-st
    if res == 2  and rs<1:
        print("#Test3-ok")
    else:
        print("#Test3-fail")


@test_nod
def get_nod(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a


@test_nod
def get_nod(a,b):
    if a<b:
        a,b = b,a
        while b!=0:
            a,b = b,a%b

        return a






