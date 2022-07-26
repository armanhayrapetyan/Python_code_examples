def Funkc(arr,pop):
    result = [arr[i]*pop for i in range(len(arr)) if arr[i]%2==0]
    print(result)

Funkc([9,8,7,6,5,4,3,2,1],9)


result = map(lambda a,b:a+b, [6,9,8,53,9,6,6],[9,7,6,5,4,1,2])

print(list(result))


def Main(a):
    if a%2 == 0:
        return a

result = filter(Main, [9,6,5,4,7,3,2])

print(list(result))

import functools


def multipiler(a,b):
    return a+b

arr = [9,8,7,4,63,2,15,4]

result = functools.reduce(multipiler,arr)

print(result)


from abc import ABC,abstractmethod

class Car(ABC):


    def __init__(self, speed,year):
        self.speed = speed
        self.year = year

    @abstractmethod
    def speed(self,speed):
        pass

    @abstractmethod
    def year(self,year):
        pass

    def getSpeed(self,speed):
        return self.speed

    def getYear(self,year):
        return self.year


class Machine(Car):
    def __init__(self,speed,year,color):
        super().__init__(speed,year)
        self.color = color

    def speed(self,speed):
        return self.speed

    def year(self,year):
        return self.year


    def getColor(self,color):
        return self.color

    def __repr__(self):
        return f" { self.speed}, {self.year}, {self.color}"


myCar = Machine("100","2021","Green")
myCar1 = Machine("250","2022","Red")
my_car_list = [myCar,myCar1]
for i in my_car_list:
    print(i)


#iteratable object

data = [9,8,6,5,4,3,2]
data1 = [9,3,5,4,7,8,9]

result = zip(data,data1)
for i in result:

    print(i,end=',')


a= int(input("Enter number "))

b = a if a%2 == 0 else "uneven"

print(b)

class Mlass:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __del__(self):
        print("Deleted Addres object " + str(self))


ob = Mlass(12,20)
print(ob.__dict__ )

#Pattern Singletion

class Point:
    __instance = None

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __init__(self,a,b):
        self.a = a
        self.b = b


    def get_result(self):
        return (self.a,self.b)

ob = Point(1,2)
ob1 = Point(10, 20)
a = ob.get_result()
b = ob.get_result()
print(id(a))
print(id(b))

class Mlass:
    a =0
    b= 100

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def result(self):
        return self.x,self.y

    @classmethod
    def funkc(cls,arg):
        return cls.a<= arg <=cls.b


ob = Mlass(1,2)
d = Mlass.result(ob)
print(d)


class Person:

    def __init__(self,name,old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self,old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


ob = Person("Arman", 20)
ob.old = 22
del ob.old
print(ob.__dict__)


class Person:
    num = 10
    def __init__(self,name,old):
        self.name = name
        self.old = old

    @classmethod
    def get_result(cls):
        return cls.num

    def __getattribute__(self, item):
        if item == "z" :
            return  ValueError("This letters is has no created method")

        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "d":
            return AttributeError("This letters has no created method")
        else:
            self.__dict__[key] = value

    def __getattr__(self,item):
        print("__getattr__: "+item)


ob = Person('Arman', 20)
a= ob.get_result()
b= ob.z
ob.m = 60
e = ob.w
print(e,ob.m,b,a)
print(ob.__dict__)



class Counter:

    def __init__(self):
        self.__counter = 0


    def __call__(self,*args,**kwargs):
        print("__call__")
        self.__counter+=args[0]
        return self.__counter

c= Counter()
a = c(5)
b= c(10)
print(a,b)


class Cords:

    def __init__(self,*args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Cords(1,-2,9)
print(len(p))
print(abs(p))


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be int")
        self.seconds = seconds % self.__DAY


    def get_time(self):
        s = self.seconds % 60   #seconds
        m = (self.seconds // 60) % 60   #minutes
        h = (self.seconds // 3600) % 24  #clocks
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")


    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("First operand must be int or Clock   ")

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c4 = c1 + c2 + c3
print(c4.get_time())


class Complex:

    def __init__(self, real, imag):
      self.real = real
      self.imag = imag


    def __add__(self, other):

        real = self.real + other.real
        imag = self.imag + other.imag

        return Complex(real, imag)

    def display(self):

        print(str(self.real) + " + " + str(self.imag) + "i")


a = Complex(10, 5)
b = Complex(5, 10)
c = Complex(4, 2)
d = a + b + c
d.display()



class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

ob = Point(1, 2)
ob1 = Point(1, 2)

print(hash(ob),hash(ob1),sep="\n")

#print(ob ==ob1)


class Mlass:
    def __init__(self,num):
        self.num  = num

    def __add__(self,other):

        num = self.num + other.num
        return Mlass(num)

    def __str__(self):
        return f"{self.num}"

ob = Mlass(2)
ob2 = Mlass(6)
ob3 = Mlass(8)
print(ob+ob2+ob3)


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self,item):
        if 0<= item <=len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Item must been this [0,len(marks)] range ")

    def __setitem__(self,key,value):
        if not isinstance(key,int):
            raise TypeError("Key must been int and big 0")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] =  value

    def __delitem__(self,item):
        if not isinstance(item,int):
            raise TypeError("Key must been int and big 0")

        del self.marks[item]


ob = Student("Arman", [5,5,5,4,10,3])
ob[10] = 7
del ob[4]
print(ob.marks)


class Point:

    def __init__(self,x,y):
        self._x = x
        self._y = y


class Cords3D(Point):

    def __init__(self,x,y,z):
        super().__init__(x, y)
        self._z = z

    def get_result(self):
        return (self._x, self._y, self._z)


ob = Cords3D(1, 2, 3)
print(ob.__dict__)
print(ob.get_result())


class Rectengle:

    def __init__(self,w,h):
        self.w = w
        self.h = h

    def get_result(self):
        return self.w*self.h


class Square(Rectengle):

    def __init__(self,w,h):
        super().__init__(w,h)


    def get_result(self):
        return 2*(self.w*self.h)


ob = Rectengle(10, 40)
ob1 = Rectengle(30, 15)
ob2 = Square(10, 10)
ob3 = Square(20, 20)


g= [ob,ob1,ob2,ob3]

for i in g:
    print(i.get_result(),end=" ")



class Point:

    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

    def get_result(self):
        return f"{self.x} {self.y}"


class  Cords:
    ID = 0
    def __init__(self,m):
        self.ID +=1
        self.id = self.ID

    def get_cords(self):
        return f"{self.id} point is a Cords class"

class Args(Point,Cords):
    pass


ob = Args(1, 2)
ob1 = Args(3,4)
print(ob.get_result())
print(ob.get_cords())
print(ob.get_cords())
print(ob.get_cords())
print(ob.get_cords())


import functools
data = [9,6,5,8,74,6]

data.sort(reverse=True)

sub = functools.reduce(lambda a,b: a-b, data)

print(sub)






