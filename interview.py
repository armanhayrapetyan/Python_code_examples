# Intervew Question
#Bad Solve O(n^2)
data = [ [10,20],[30,45],[60,79],[100,115]]
data1 = [[15,25],[30,49],[60,81],[100,220]]

dc = dict(data1)
#print(dc)
target = 20

def funkc(data,data1,target):
    for i in range(0,len(data)):
        for j in range(0,len(data1)):
            if min(data[i]) == min(data1[j]):
                if (min(data[i]) + target <= max(data[i])) or (min(data1[j]) + target <= max(data1[j])):
                    return [min(data[i]),(min(data[i])+target)] or [min(data[j]),(min(data[j])+target)]

#print(funkc(data,data1,target))

#Good solve O(n)

data = [ [10,20],[30,45],[60,79],[100,115]]
data1 = [[15,25],[30,51],[60,78],[100,120]]

#dc = dict(data1)
dc = {min(data1[i]):max(data1[i]) for i in range(0,len(data1)) }
#print(dc)
target = 20

def funkc(data,data1,target):
    for i in range(0,len(data)):
        for k,v in dc.items():
            if min(data[i]) == k:
                if (min(data[i]) + target <= max(data[i])) or (k + target <= v):
                    return [min(data[i]),(min(data[i])+target)] or [k,k+target]

#print(funkc(data,data1,target))


string = "abczabebiefcq"

def get_firs_chars(string):
    dc = {i:string.count(i) for i in string}
    print(dc)
    for k,v in dc.items():
        if v == 1:
            return f" Chars is a {k} in repeated {v} steps"

print(get_firs_chars(string))


# Google interview question

def sum_search(a,b,c):
    st = set(b)
    for i in range(len(a)):
        b = c - a[i]
        for j in st:
            if j == b:
                return "True"

    return "False"

#print(sum_search([3,2,5,4,8,7],[6,5,4,7,9,2],10))

















