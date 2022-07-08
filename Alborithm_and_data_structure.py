# # N = 191  K = 4
# def solution(N,K):
#
#     res=[int(i) for i in str(N)]
#     kb = K
#     new = []
#
#     for i in res:
#         dum = i
#         while(dum!=9):
#             if kb == 0:
#                 break
#             else:
#                 dum+=1
#                 kb-=1
#
#         new.append(dum)
#         listToStr = ''.join([str(j) for j in new])
#
#     return listToStr
#
# print(solution(512, 10))
#
#
# # N = 191  K = 4
# def solution(N, K):
#
#     i = 0
#
#     while K>0 and i<3:
#         N_str = str(N)
#         tmp = int(N_str[i])
#         if tmp ==9:
#             i+=1
#
#         else:
#             new_str =N_str[:i]+str(tmp+1) + N_str[i+1:]
#             if int(new_str) > N:
#                 N = int(new_str)
#                 K-=1
#
#     return new_str
#
# print(solution(981, 4))
#
#
# import csv
# fields = ['Name', 'Branch', 'Year', 'CGPA']
#
# rows = [['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
#
# filename = "university_records.csv"
#
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
#
# # Python3 code to find duplicates in O(n) time
#
# numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
# arr_size = len(numRay)
# for i in range(arr_size):
#
# 	x = numRay[i] % arr_size
# 	numRay[x] = numRay[x] + arr_size
#
# print("The repeating elements are : ")
# for i in range(arr_size):
# 	if (numRay[i] >= arr_size*2):
# 		print(i, " ")
#

# class Point1:
#     def __init__(self,x,y):
#         self.x  = x
#         self.y = y
#
# class Cords3D(Point1):
#
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z = z
#
#ob = Cords3D(1,2,3)
# ob1 = Point1(1,2)
# print(ob1.__dict__)
# print(ob.__dict__)

import math
def Base(dx = 0.0001):
    def DerivateBase(func):

        def Derivate(x):
            return (func(x+dx)-func(dx)) / dx

        return Derivate
    return DerivateBase

@Base(dx = 0.001)
def der_sin(x):
    return math.sin(x)


# Base = Base(0.001)
# der_sin = Base(der_sin)
# der_sin = Base(0.001)(der_sin)
df  = der_sin(math.pi/3)
print(df)






