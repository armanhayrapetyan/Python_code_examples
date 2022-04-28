
List = [x**2 for x in range(5)]
List = List.pop()+16
print(List)


def fun(x,y = [3,5]):
    y.append(x)
    return y


print(fun(2,[2,4]))

List = ['P','Y','T','H','O','N']

for i in enumerate(List):
    print(i,end="")

#none type
def funkc():
    pass

print(type(funkc()))

# 1 3 6 10
List1 = [1,2,3,4]
List2 = []

for x in range(0,4):
    List2.append(sum(List1[0:x+1]))

print(List2)

#[[5], [5], [5]]
List = [[]]*3

List[1].append(5)

print(List)

# 0 1 2 2
List = [0,1,2,3]

for List[-1] in List:
    print(List[-1],end=" ")

data = [9,6,2,4,8,7,3,1,0]


def getresult(data):

    dc = {x: x for x in data}
    print(dc)
    for i in range(len(dc)):
        if i not in dc:
            return i

print(getresult(data))



data = [[1,2,3],[4,5,6],[7,8,9]]


data1 = [ [x**2 for x in row] for row in data]
print(data1)

#Zamekanie
def point(name):

    def num():
        print(f"Hayrapetyan {name}")

    return num

a = point("Arman")
a()

def get_res():
    for i in range(0,50):
        a = range(i,50)
        yield sum(a)/len(a)


p = get_res()
print(list(p))



# 192   #4

def solution(N,K):
    i = 0
    while i>3 and k>0:
        N_str = str(N)
        tmp = N_str[0]
        if tmp == 9:
            i+=1
        else:
                new_N_str = N_str[:i] + str(tmp+1)+N_str[i+1:]
                if int(new_N_str) >n:
                    N = int(new_N_str)
                    K-=1

    return N

p = solution(192,4)
print(p)


data = [3,2,0,1,5,4,9,7]
#data.sort()

def getElement(data):
    for index,value in enumerate(data):
        #print((index,value),end="\n")
        if index !=value:
            return index


    return len(data)+1

p =getElement(data)
#print(p)

dc = {x:x for x in data}
print(dc)

def getElement1(data):
    for i in range(len(dc)):
        if i not in dc:
            return i

    return len(dc)+1

print(getElement1(data))


class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]

        for index , record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))


    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        for index, record in  enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                return record

        return "Record Not found"

    def __str__(self):
        return str(self.hash_table)

hash_table = HashTable(100)
hash_table.set_val("arman@gmail.com","Arman Hayrapetyan, 2000, Armenia")
hash_table.set_val("gevor@gmail.com","Gevor Manukyan, 2001, Armenia")
print(hash_table)
print(hash_table.get_val("sahak@gmail.com"))
import math


data = [7,5,10,24,9,7,5]
# 10 24 7 5 9 7 5 
data.sort(key=lambda a : a%2 ==0,reverse=True)
print(data)  

data = [6,2,1,1,5,1,1,4]

rs = max(data, key=data.count)
ls = data.count(rs)
#print(rs , ls)

from statistics import mode

rs = mode(data)
ls= data.count(rs)
print(rs,ls) 


data = [6,5,8,9,10,25,65,3,11,13]

rs = filter(lambda a: 10<a<15,data)

#print(list(rs))


data = []
def funkc(start,end):
    for i in range(start,end):
        if i % 2==0:
            data.append(i)

    return data

#print(funkc(1,10))

def adf():
    start = int(input("Enter start number "))
    end = int(input("Enter end number "))

    rs = filter(lambda a :a%2 ==0, range(start,end))
    #print(list(rs))
    #print("===============================")
    adf()

adf()   


tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]


rs = filter(lambda t:t, tuples)
print(list(rs))  


def comulative(data):
    new_arr = []
    length = len(data)
    sum_list = [sum(data[0:x:1]) for x in range(0,length+1)]

    return sum_list[1:]

print(comulative([10,20,30,40,50])) 


data = [6,3,2,5,4,7,9]

data.remove(max(data))
print(max(data))


data = [0,0,1,2,3,0,0,0,0,1,2,3]

def solution(data):
    b= 0
    maxb = 0
    for i in data:
        if int(i) ==0 :
            b+=1
        elif int(i) !=0:
            maxb = max(maxb,b)
            b = 0

    return maxb

print(solution(data))


data = [[6,5,8,7,7],
        [6,2,5,7,9],
        [-3,1,9,10],
        [3,6,9,85,4],
        [98,32,65,47]]

ls = []
def solution(data):
    for i in range(0,len(data)):
        S = (sum(data[i]),i)
        ls.append(S)
        ls.sort(reverse=True)

    return ls

print(solution(data))  


# Algorithm KMP
a = "AABAACAADAABAABA"
t = "AABA"

p = [0]*len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("face found ")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n and j != m:
    print("face found ")

# Derivetaing math function with class

import math

class Derivete:

    def __init__(self,func):
        self.__fn = func

    def __call__(self, x, dx=0.0001 ,*args, **kwargs):
        return (self.__fn(x+dx)-self.__fn(x))/dx


@Derivete
def def_sin(x):
    return math.sin(x)


p = def_sin(math.pi/4)
print(p)













