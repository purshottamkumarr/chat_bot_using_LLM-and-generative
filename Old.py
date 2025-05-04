# height = int(input("Enter your height ?"))
#
# if height >= 5:
#     print("can ride")
#     age = int(input("Enter your age:"))
#     if age <= 20:
#         print("Please pay Rs 250:")
#
#     else:
#         print("pleaae pay Rs 500")
# else:
#     print("cant ride:")

# for i in range(0, 100):
#     print("Jai shree ram")

# for i in range(0, 100):
#     print("jai shree ganesh")

# def printLordName(str):
#     for i in range(0, 100):
#         print(str)
#
#
# printLordName("jai shree ram")


# def searchInList(list, target):
#     flag = False
#     index = -1
#     for i in range(0, len(list)):
#         if (list[i] == target):
#             flag = True
#             index = i
#             break
#
#     if flag == True:
#         print(target, " is availble on index ", index)
#     else:
#         print("Not available")
#
#
#
# list = [7,4,9,5,4,1,6,9]
# searchInList(list, 45)
#
# list = [4,9,6,3,4,5,8,9]
# searchInList(list, 9)



# list = [12,45,36,95,74,12,65,32,78]
#
# for i in range(0, len(list)):
#     print(list[i])

# list = [4,1,2,6,4,8,9]
# for i in range(0, len(list)):
#     print(list[i])
# #
# # 4,1, 2, 6
# #
# # i = 0,
# # lits[0]=4
# # i = 1
# # lit[1]= 1
# # i=2
# # list[2]=2
# # i=3
# # list[3]=6
# # i = 4
# # list[4]=4
# i = 5
# list[5]=8
# i = 6
# list[6] = 9

# list = [8,4,5,6,9]
# list2=[]
# for i in range(0, len(list)):
#     list2.append(list[i]+5)
#
# print(list)
# print(list2)

# def purshottam (str):
#     for i in range(0,50):
#         print(str)
# print("jai shrre ram")
# print("ram")

#create array example

# import array
# student_roll=array.array("i",[101,102,103,104,105])
# print(student_roll[3])

# list=[1,4,6,4,6,7]
# for i in range (0,len(list)):
#     print(list[i]+5)

# from array import *
# student_roll=array("i",[101,204,409,503])
# for element in student_roll:
#     print(element)
#
# lenght=len(student_roll)
# print(lenght)
# for i in range(lenght):
#     print(student_roll[i])

# from array import *
# student_roll=array("i",[103,105,208,409,309,406])
# length=len(student_roll)
# print(length)

# i=0
# while(i<=length):
#     print(student_roll[length])
#     i+=1
#  print("my name is purshottam")

# from array import *
# student_name= array("i",[2,3,4,5,6,7,8])
# length=len(student_name)
# print(length)
# i=0
#

# from array import *
# student_name=array("i",[102,103,108,109,111])
# length=len(student_name)
# print(length)
# i=0
# while(i<=length):
#     print("student_name"[length])
#     i+=1
# print("student_name"[length])


# # getting input from user :
# from array import *
# student_no=array("i",[])
# roll_no= int(input("enter the element:"))
# for i in range(roll_no):
#     student_no.append(int(input("enter the element:")))
# for i in range(len(student_no)):
#     print(student_no["i"])


#getting input from user while loop

# from array import *
# student_no=("i",[])
# p=int(input("enter the no elemnt"))
#
# i=0
# j=0
# while(i<p):
#     i+=1
# while(j<len(student_no)):
#     print(student_no[j])
#     j+=1

#pop()

# from array import *
# yarnex_exhibition= array("i",[102,104,105,106])
# p=len(yarnex_exhibition)
#
# i=0
# while(i<p):
#     print(yarnex_exhibition[i])
#     i+=1
# yarnex_exhibition.pop()
# p=len(yarnex_exhibition)
# i=0
# while (i<p):
#     print(yarnex_exhibition[i])
#     i+=1




# if statement:
# if (5>2):
#  print("grater")
#
# a=int(input("enter the no greater then 2:"))
# if(a>2):
#  print("you have entered",a)

# nested if statement
# if(5>2):
#  print(" 5 is grater than 2")
#  if(6>2):
#   print("6 is grater than 2")
#
# print("rest of code")

# if elif statement

# a=20
# b=30
# if(a>=b):
#  print("a is grater than b")
# elif(a==b):
#  print("a and b are equal")
# elif(a<b):
#  print("a is less than b")

# day="tuesday"
# if(day=="monday"):
#  print("today is monday")
# elif(day=="tuesady"):
#  print("today is tuesday")
# elif(day=="wednesday"):
#  print("today is wednesday")
# else:
#  print("today is sunday")

# while loop
#
# a=2
# while(a<=20):
#  print(a)
#  a+=5


#while loop with else:

# a=2
# while(a<20):
#  print(a)
#  a+=1
# else:
#  print("while condition are false")


# p=4
# while (p<50):
#  print("outer loop ",p)
# p+=2
#
# q=5
# while(q<40):
#  print(q)
#  q+=4

#for loop

# str="purshottam"
#
# for k in "purshottam":
#  print(k)

#for loop with range

# a=range(5)
# for k in a:
#  print(k)

# a=range(1,5)
# for p in a:
#  print(p)


# a=range(1,20,4)
# for c in a:
#  print(c)

# name="purshottam"
# for n in name:
#  print(n)
# else:
#  print("rest of the code")


#dictionary
#purshottam={}

# student_name={101:"anajali",104:"nikki",108:"nikita",109:"pooja"}
# print(student_name[101])
# student_name[107 ]="chotu"

# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()


# from numpy import*
# student_no= array([101,103,104,105,108,109])
# n=len(student_no)
# print(n)
# for axio in range(n):
#     print(axio,student_no[axio])

# from numpy import*
# a=linspace(1,8,5)
# print(a[0])
 # print(a[1])
# print(a[2])

# from numpy import*
# a=linspace(1,8,5)
# for pu in a:
#     print(pu)

# from numpy import*
# a=linspace(1,10,4)
# b=len(a)
# print(b)
# for nikki in range(b):
#     print(nikki)
#     print(a[nikki])
#     nikki+=1

# from numpy import*
# a=linspace(1,10,4)
# n=len(a)
# k=0
# while


# a=15
# print(a<<2)

# from numpy import*
# m=int(input("enter the no of row:"))
# n=int(input("enter the no of column:"))
# a=zeros((m,n),dtype=int)
# print(a)
# u=len(a)
# print(u)
# for i in range(u):
#     for j in range(len(a[i])):
#         x=int(input("enter the element:"))
#         print(a[i][j])

# from numpy import*
# k=int(input("enter the no of element:"))
# a=zeros(k,dtype=int)
# for p in range(k):
#     n=len(a)
#     print(n)
#     k=int(input('enter the element:'))
#     q=a[p]
# print(a)


# from numpy import*
# a=int(input("enter the element:"))
# b=zeros(a,dtype=int)
# c=len(b)
# print(c)
# i=0
# j=0
# while(i<c):
#     d=int(input("enter the element"))
#     e=a[i]
#     i+=1
# print(a)

# from numpy import*
# a=array([1,2,3,4,5,6])
# b=reshape(a,(2,3))
# print(a)
# print(b)

# from numpy import*
# a=array([[1,2,3,4,5],[6,7,8,9,10]])
# b=e.flatten()
# print(a)
# print(b)

# from numpy import*
# k=array([[1,2,3,4],
#          [6,7,8,9],
#          [10,11,12,13]])
# print("original array")
# print(k)
# print(k[0])
# print(k[1])
# a=k[2,:]
# print(a)

#print("purshottam " * 5)


# def func():
#     list,list2 =[7],[7]
#     list3=list * 2
#     return list3==list.extend([list])
# print(func())

# def func(x):
#     return x * 2
# result=func(2)
# result=func(result)
# result=func(result)
# print(result)

# def manvi():
#     name="purshottam"
#     print("welcome to",name)
#     manvi()

#height=int(input("enter height in feet:"))

#if(height>3):
    # print("buy token")
#print("now you can buy car")
#print ("pooja rani")

#else:
    #print("no token required")

# height=int(input("enter the height in feet:"))
# if(height>3):
#      print("buy token")
# else:
#      print("no token required")

#height=int(input("enter height in feet:"))

#if(height>3):
    # print("buy token")
#print("now you can buy car")
#print ("pooja rani")

#else:
    #print("no token required")

# height=int(input("enter the height in feet:"))
# if(height>3):
#      print("buy token")
# else:
#      print("no token required")

# input("what is your name?")
# print("hello " + "purshottam")
# print("hey "+" " + input("what is your name?")+" " + "how are you")

# year=int(input("which year you want to check?"))
# if year % 4==0:
#     if year % 100==0:
#         if year % 400==0:
#             print("leap year.")
#         else:
#             print("not leap year.")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

# import random
# user_choice= int(input("Enter your choice: Type 0 for rocks, Type 1 for paper, type 2 for scissors: "))
# computer_choice= random.randint(0,2)
# print("computer choose:")
# print("user_choice:")
# if computer_choice == user_choice:
#     print("its draw")
# elif computer_choice > user_choice:
#     print("loose")
# elif user_choice > computer_choice:
#     print("you will win")
# elif computer_choice ==0 and user_choice == 2:
#     print("you will loose")
# elif  user_choice == 0 and computer_choice ==2 :
#     print("you will win")

# numbers= [10,0,-1,-3,6,9,45,48]
#print(numbers)
#names=["pooja","purshottam","nikki"]
#print(names)
#mix_list=[1,"pooja","anjali",-1,10.10]
#print(mix_list)
#print(len(numbers))
#print(numbers[-1])
#print(numbers[0:4])
#print(numbers[1:5])
#print(numbers[:5])
#print(numbers[0:5:1])
#print(numbers[0:5:3])
#print(numbers[0::3])

# numbers.sort()

#print(numbers)
#print(min(numbers))
#print(max(numbers))
#numbers.append(69)
#print(numbers)
#numbers.insert(3,70)
#print(numbers)
#numbers.extend([23,56,67,89,67,89])
#print(numbers)
#numbers[0]=56
#print(numbers)
#numbers.remove(-1)
#print(numbers)
# numbers.pop()
# print(numbers)
# print(numbers.pop())
# print(numbers.pop(-3))

numbers= [10,0,-1,-3,6,9,45,48]
#print(numbers)
#names=["pooja","purshottam","nikki"]
#print(names)
#mix_list=[1,"pooja","anjali",-1,10.10]
#print(mix_list)
#print(len(numbers))
#print(numbers[-1])
#print(numbers[0:4])
#print(numbers[1:5])
#print(numbers[:5])
#print(numbers[0:5:1])
#print(numbers[0:5:3])
#print(numbers[0::3])

# numbers.sort()

#print(numbers)
#print(min(numbers))
#print(max(numbers))
#numbers.append(69)
#print(numbers)
#numbers.insert(3,70)
#print(numbers)
#numbers.extend([23,56,67,89,67,89])
#print(numbers)
#numbers[0]=56
#print(numbers)
#numbers.remove(-1)
#print(numbers)
# numbers.pop()
# print(numbers)
# print(numbers.pop())
# print(numbers.pop(-3))


# class - class is a blueprint for an object. like - real world enity has some properties or behaviour,
#         which is represented by class variable and method in python.

# object : as we know class is a logical enity
            # while an object is a physical or real entity that works on class data

# constructor: The first method __init__() is a special method,
                # which is called class constructor or initialization method that Python calls
#                   when you create a new instance of this class
# access of class variable / method: You access the object's attributes using the dot operator with object.
#                                   Class variable would be accessed using class name

# self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
#
# The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on
#

# class human:
#     def __init__(self, height, widh):
#         print(height, widh)
#
#     def read(self, subject):
#         print(subject)
#     def laugh(self,good):
#         print(good)
#
# obj = human(50, 60)
# obj.read("physics")
# obj.laugh("health")

# class Person:
#     def __init__(self):
#         self.age = 10
#         self.weight = "80kg"
#         self.height = "5.5ft"
#
#     def fun(self):
#         print(self.age, self.weight)
#
# obj = Person()
# obj.fun()

# class neelam:
#     def __init__(self,age,name,address):
#         print(age," ",name," ",address," ")
#
# object=neelam(20,"purshottam","koreya")
# object2=neelam(30,"pooja","gurpa")
# object3=neelam(40,"nikki","gaya")
# object4=neelam("anjali","priyanka","preet")

#
# class a:
#     def __init__(self):
#         self.name=""
#         self.age=""
#         self.address=""
#     def setData(self, age, name, address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def showData(self):
#         print(f"{self.name} {self.address} {self.age}")


# a_obj = a()
#
# a_obj.setData(25, "Deepu", "Gaya")
# a_obj.showData()
# a_obj.setData(25, "purushottam", "gaya")
# a_obj.showData()

# class calculator:
#     def __init__(self, a , b):
#         self.x = a
#         self.y = b
#     def sum(self):
#         print(self.x + self.y)

#     def subtract(self):
#         print(self.x-self.y)
#
#     def multiply(self):
#         print(self.x * self.y)
#
#     def devide(self):
#         print(self.x % self.y)
#

# cal = calculator(8, 4)
# cal.sum()
# cal.subtract()
# cal.multiply()
# cal.devide()


# class Employee:
#     def __init__(self):
#         self.name=""
#         self.address=""
#         self.salary=""
#         self.count = 0
#         self.data=[]
#
#     def setEmployeeData(self, name, address, salary):
#         self.name=name
#         self.address=address
#         self.salary=salary
#         self.count+=1
#         self.data.append({"name":name, "address":address, "salary":salary})
#
#     def displayEmployee(self):
#         print(f"{self.name}-{self.address}-{self.salary}")
#
#     def showAllData(self):
#         for i in range(0, len(self.data)):
#
#             print(f"name: {self.data[i]['name']} , address: {self.data[i]['address']}, salary: {self.data[i]['salary']}")

#     def lengthofdata(self):
#         print(len(self.data))


# emp_obj = Employee()
# emp_obj.setEmployeeData("Pooja", "Gaya", "25000")
# emp_obj.setEmployeeData("purushottam", "Gaya", "35000")
# emp_obj.setEmployeeData("Deepu", "Gaya", "35000")
# emp_obj.showAllData()
# emp_obj.lengthofdata()

# str = "this is a string"
# value = str.split(" ")
# print(value)
# value2 = "+".join(value)
# print(value2)



# class person:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
# ram = person("purshottam",25,"koreya")
#
# print(ram.name)
# print(ram.age)
# print(ram.address)

# class axio:
#     def __init__(self,name,salary,incetives):
#         self.name = name
#         self.salary = 30000
#         self.incetives =5000
#     def my_love(self):
#         print("my name is hello " + self.name,self.salary,self.incetives)
# a = axio("axio",3000,5000)
# a.my_love()

# Oop: Object oriented programing
# it is a programing aproach based on class and object
# Oop is the method to represent the real world entity

# feature of oops
# 1. Class and object
# 2. encapsulation
# 3. inheritance
# 4. abstraction.
# 5. pollymorphism

# class A:
#     __x=10 #make private member synt = __VariableName
#     _y=20  #make Protected  member synt = __VariableName
#     def printxvalue(self):
#         print(self.__x)
#
# boj=A()
# boj.printxvalue()
# print(A._y)

# function = method = function
# class A:
#     x=20 #public
#     __x=10 #private
#     _x=50 #protected
#
#     def __int__(self, a, b):
#         print(a, b)
#     def __init__(self, a, b):
#         print(a, b)
#
#     def set(self, a, b):
#         print(a, b)
#
#     def set(self, a, b, c):
#         print(a, b, c)
#     def get(self):
#         print("self.__x")

# access modifier
# public
# private
# protected

# obj=A(4,5)
# obj.get()
# print(obj.x)
# print(A.x)
# print(A._x)
# print(obj._x)

# Example no 1

# class Myclass:
#     def show(self):
#         print("i love my mom")
# object = Myclass()
# object.show()

# Example 2

# class Mobile:
#     def __init__(self):
#         self.model1 = "oppo"
#         self.model2 ="vivo"
#         self.model3 = "apple"
#     def show(self):
#         print(self.model1,self.model2,self.model3,"model")
#
# # object = Mobile()
# # # object.show()
# print(object.model1)

# class Mobile:
#     def __init__(self):
#         self.model = "oppo"
#         self.model2 = "vivo"
#         self.model3 = "Realme"
#     def show(self):
#         price1 = 1000
#         price2 = 2000
#         price3 = 3000
#         print(self.model,self.model2,self.model3,"Model","price:" ,price1, "price:",price2,"price:",price3)
#
# pooja = Mobile()
# pooja.show()

# class Mobile:
#     __list=[]
#     def __init__(self):
#        self.__list=[]
#     def setModel(self, model1, mode1price):
#         self.__list.append({model1, mode1price})
#
#     def show(self):
#         print(self.__list)

# pooja = Mobile()
# pooja.setModel("sumsung", 3000)
# pooja.setModel("opo", 5000)
# pooja.setModel("vivo", 8000)
# pooja.setModel("realme", 7000)
# pooja.show()

#
# def my_func(pooja:tuple):
#     if any(pooja):
#         return("i love it")
#     else:
#         return("my heart is empty")

# nikki = ()
# result = my_func(nikki)
# print(result)



# jab hm koi class define krte hai  or o class ke member ko
# koi dusra class access karta hai to is condition me inheritance kahte hai.
# when we define a class that inherit all the properties/member of other class is called inheritance

# class= capital , function = camel case - deepuKumar

# class Father():
#     def land(self):
#         print("50 bigha ")
#
# class Son(Father):
#     def money(self):
#         print("100 rupya")
#
#
# son_obj = Son()
# son_obj.money()
# son_obj.land()

# class A():
#     x=10
#     y=20
#     def sum(self):
#         return self.x+self.y

# class B(A):
#     def subtract(self):
#         return self.x-self.y


# b_obj = B()
# print(b_obj.subtract())
# print(b_obj.sum())

# type of inheritance
#
# 1. Simple Inheritance or single Inheritance
# 2. multiple Inheritance
# 3. Multilevel inheritance
# 4. hirarichal inheritance
# 5. Hybrid inheritance

# class A:
#     x=10
#     y=20
#     def sun(self):
#         print(self.x+self.y)
#
# class B(A):
#     def subtraction(self):
#         print(self.x-self.y)


# multiple Inheritance

# class Ram:
#     first_bro = "Bharat"
#     second_bro = "Lakshman"
#     third_bro = "Shatru"
#     def displayRamBrother(self):
#         print(self.first_bro+" "+self.second_bro+" "+self.third_bro)
#
# class Ravan:
#     first_brother = "Vibhison"
#     second_bro = "kumbhkaran"
#     def ravanBrother(self):
#         print(self.first_brother + self.second_bro)
#
# class Hanuman(Ram, Ravan):
#     Full_Nam = "Pavan Putr Hanuman"
#     Father_name = "Pavan Deo"
#     MOther_name = "Anjali mata"
#     def aboutHanuman(self):
#         print(self.Full_Nam+" "+ self.Father_name +" " + self.MOther_name)

# object = Hanuman()
# object.aboutHanuman()
# object.displayRamBrother()
# object.ravanBrother()

# // multi-level

# class Father:
#     def land(self):
#         print("50 bigha")
#
# class child1(Father):
#     def money(self):
#         print("100 rupya")
#
# class child2(Father):
#     def money(self):
#         print("200 rupya")
#
# class child3(Father):
#     def money(self):
#         print("300 rupya")

# obj_child1=child1()
# obj_child1.land()
#
# obj_child2 = child2()
# obj_child2.money()


# harerichal

# class A:
#     x = 10
#
# class B(A):
#     y=20
#
# class C(B):
#     z=50
#
# class D(C):
#     w = 90
#
# obj_d=D()
# print(obj_d.x)
#
# obj_c=C()
# print(obj_c.y)

# single inheritance

# class Parents:
#     def display(self):
#         print("parent")
# class child (Parents):
#     def show(self):
#         print("child")
#
# k_1 = child()
# k_1.show()
# k_1.display()

# multi level inheritange

# class Granffather:
#     def gdisplay(self):
#         print("grandparent")
#
# class Parents(Granffather):
#     def pdisplay(self):
#         print("parents")
#
# class child (Parents):
#     def cdisplay(self):
#         print("child")
#
# p1 = child()
# p1.cdisplay()
# p1.pdisplay()
# p1.gdisplay()

# Hierarchical inheritange

# class Parents:
#     def pdisplay(self):
#         print("Parents")
#
# class Child_1(Parents):
#     def cdisplay(self):
#         print("child")
#
# class child_2(Parents):
#     def kdisplay(self):
#         print("child")
#
# c_1 = Child_1()
# c_1.pdisplay()
# c_1.cdisplay()
#
# c_2 =child_2()
# c_2.pdisplay()
# c_2.kdisplay()


# multiple inheritange

# class Father:
#     def fdisplay(self):
#         print("father")
#
# class Mother:
#     def mdisplay(self):
#         print("mother")
# class Child(Father,Mother):
#     def cdisplay(self):
#         print("child")
#
# p_1 = Child()
# p_1.cdisplay()
# p_1.mdisplay()
# p_1.fdisplay()

# class Parents:
#     def gdisplay(self):
#         print("parents")
#
# class Child(Parents):
#     def kdisplay(self):
#         print("child")
#
# l_1 = Child()
# l_1.kdisplay()
# l_1.gdisplay()

# class Grandfather:
#     def gfather(self):
#         print("grand father")
#
# class Parents:
#     def parentdisplay(self):
#         print("parents")
#
# class Mother:
#     def maparentsdisplay(self):
#         print("mother")
#
# class child(Parents,Mother):
#     def lchilddisplay(self):
#         print("child")
#
# p_1 = child()
# p_1.lchilddisplay()
# p_1.maparentsdisplay()
# p_1.parentdisplay()


# polymorphism -

# poly - many
# morphis - forms
# polymorphism means ability totake various forms (some object having differet behaviour)

# print(5+5) - sum
# print("5"+"5") - concatinate
# print(len("purushotam"))
# print(len(["purushotam", "puja"]))

# there are two type of polymorphism
# 1. overloading
# 2. overriding


#
# overloading-

# class A:
#     def sum(self, x, y):
#         print(x+y)
#     def sum(self, x, y, z):
#         print(x+y+z)
#
# a_obj = A()
# a_obj.sum(5, 10)


# class MethodOverloading:
#     def multiply(self, x, y):
#        print(x*y)
#
#     def multiply(self, x, y, z):
#        print(x*y*z)
#
# obj = MethodOverloading()
# print(obj.multiply(2, 3))
# print(obj.multiply(2, 3, 4))

# method = function = method
# class A:
#     def show(self, firstName="", lastName=""):
#         print(firstName, lastName)
#
# obj = A()
# obj.show()
# obj.show("Deepu")
# obj.show("Deepu", "Kumar")



# class B:
#     def sum(self, x=0, y=0):
#         print(x+y)
#
#     def sum(self, x=0, y = 0, z=0):
#         print(x+y+z)
#
# obj = B()
# obj.sum(7,8)
# obj.sum(9)
# obj.sum(7,9,5)
# obj.sum(9,8,5)


# class P:
#     def sum(self,x=2,y=1,):
#         print(x+y)
#
#     def sum(self,x=1,y=1 ,z=1,p=1):
#         print(x+y+z+p)
#
# sum_1 = P()
# sum_1.sum(7,8,5)
# sum_1.sum(3)

# list = [1,2,3,4,5 ]
# new_list = [ i * i for i in list if i % 2 == 0]
# print(new_list)

# class Mobile:
#     Fp = "yes"
#     def __init__(self):
#         self.model = "Realme x"
#
#     def show_model(self):
#         print("model:",self.model)
#
#     @classmethod
#     def is_Fp(cls):
#         print("finger print",cls.Fp)
#
# realme = Mobile()
# realme.show_model()
# Mobile.is_Fp()
# Mobile.Fp = "no"

# class mobile:
#     fp = "no"
#     @classmethod
#     def my_love (cls):
#         print(cls.my_love)
#
# realme = mobile()
# print(mobile.fp)
# mobile.my_love()

# class Mobile:
#     Ram = "Sita"
#     def __init__(self):
#         self.model = "Realme X"
#
#     def show_model(self):
#         print(self.model)
#
#     @classmethod
#     def is_Ram(cls):
#         print("finger print:", cls.Ram)
#
# realme = Mobile()
# realme.show_model()
# print(Mobile.Ram)

# class pooja:
#     Ram = "Sita"
#     def __init__(self):
#         self.make = "oppo"
#         self.model = "vivo"
#
#     @classmethod
#     def love(cls):
#         print("i am in love:",cls.Ram)
#
#     def show_model(self):
#         print(f"{self.make},{self.model}")
#
# Laxman = pooja()
# print(pooja.Ram)
# Laxman.show_model()


# overriding
# class parent:
#     def culture(self):
#         print("manday ko puja hota hai")
#
#
# class child(parent):
#     def culture(self):
#         super().culture()
#         print("wednesday ko ab puja hoga.")
#
#
# child_obj = child()
# child_obj.culture()

# class A:
#     def sum(self, x, y):
#         print(x*y)
#
# class B(A):
#     def sum(self, x, y):
#         print(x+y)
#         super().sum(x, y)
#
# b_onj = B()
# b_onj.sum(7,8)


# list = [2, 3, 5, 1, 7, 8, 6, 5, 5, 7, 7, 7, 8]
#
# counter = 0
# i = 0
# while i < len(list)-1:
#     if list[i] == 8:
#         counter += 1
#     i += 1
#
# print(counter)

# a =  [7,4,-9,-5,4,-6,-8,2,1,0,0,0,]
#
#  -5,-6,-8,-9,0,0,0,1,2,4,4,7
#
#  a= [-9,-8,-6,-5,0,0,0,1,2,4,4,7]
#
# for i in range(0, len(a)-1):
#     for j in range(i+1, len(a)):
#         if(a[i]>a[j]):
#             temp = a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a)

# p= 155
# print(p>>2)

# str = "pur usho tam puja"
# str2=""
#
# for i in range(0, len(str)):
#     if(str[i]==" "):
#         pass
#     else:
#         str2+=str[i]
#
# print(str2)

# list = [1,1,4,4,8,4,5,9,6,7,2,4,]
#
# pooja = 0
# i = 0
# while i<len(list)-1:
#     if list[i] == 1:
#         pooja +=1
#     i+=1
# print(pooja)


# y =  [7,4,-9,-5,4,-6,-8,2,1,0,0,0,]
#
# for i in range(0,len(y)-1):
#     for j in range(i+1,len(y)):
#
#         if (y[i]>y[j]):
#             temp =y[i]
#             y[i] = y[j]
#             y[j] =temp
# print(y)
#

# str = "pur usho tam puja"
# str_2 = ""
# for i in range(0,len(str)):
#     if (str[i] ==""):
#         pass
#     else:
#         str_2+= str[i]
#
# print(str_2)

# for i in range(2, 49/2):
#     if(49/i == 0)
#         print(this is not prime number)
#
# print("this is prime number")
# jo apne aap se or 1 se devide ho = prime number
# 769

# 49
# 24.5
# 1, 2, 3, 5, 7, 11,13,17,19
#
# 769/2
#
# 2 - 769/2

# 9
# 15
# 2 %15 = 0
# 3 % 15 = 0


# num = input("enter the number")
# n = int(num)
# flag = True
# for i in range(2, n//2):
#     if n % i == 0:
#         flag = False
#
# if(flag):
#     print("prime Number")
# else:
#     print("not prime number")
#


# a=[7,8,4,5,6,9,8,7,4]
# b= [1,4,5,6,4,7,8,9]
#
# c= a+b
# print(c)
#
# for i in  b :
#     a.append(i)
# print(a)


# class employee :
#     def getdate(self):
#         self.name = "pursottam"
#         self.age = "28"
#
#     def putdata(self):
#         print("name\t:", self.name)
#         print("age\t:",self.age)
#
# object = employee()
# object.getdate()
# object.putdata()

# class date:
#     def get_data(self):
#         self.dd = ("enter date (dd)")
#         self.mm = ("enter the month(mm)")
#         self.yy =("enter the year(yy)")
#
#     def display(self):
#         print(self.dd, ":",self.mm, ":",self.yy,":")
# object = date()
# object.get_data()
# object.display()


# class emolyee:
#     def __init__(self):
#         def get_data(self):
#             self.name = ""
#             self.age  = ""
#
#         def put_data(self):
#             print(self.name,":",self.age ,":")
#

# class employee:
#     def get_data(self):
#         self.name = "purshttam"
#         self.age  = 28
#
#     def getupdate(self):
#         print(self.name,":",self.name, ":")
#
#     def __init__(self,name ,age):
#         self.name = name
#         self.age  = age
#
# object = employee()
# object.get_data()
# object.getupdate()
# object2 = employee()
# object2.employee("purshottam",28)


    # *   *   *   *
    # *   *   *   *
    # *   *   *   *
    # *   *   *   *



# for i in range(0, 4):
#     for j in range(0, 4):
#         print("* ", end="")
#     print("\n")





    # *
    # *   *
    # *   *   *
    # *   *   *   *



# n = int(input("enter the no rows"))
# p = 1
# for i in range (0,n):
#     for j in range(1,i+2):
#         print("*",end = " ")
#     print("\n")




    # *   *   *   *
    # *   *   *
    # *   *
    # *


# for i in range(0, 4):
#     for j in range(0, 4-i):
#         print("* ", end = "")
#     print("\n")



# row = int(input("Enter No of row: "))
# col = int(input("Enter No of column: "))
# for i in range(0, row):
#     for j in range(0, col):
#         print("* ", end="")
#     print("\n")


#
# n = int(input("enter the no rows"))
# k = 1
# for i in range (n):
#     for j in range(1,i+2):
#         print("*" , end= " ")
#     print("\n")






#             *
#         *   *
#     *   *   *
# *   *   *   *

# 1. devide bt 2 part
#     print space
#     print * according to row

# for i in range(0, 5):
#     for j in range(0, 5-i):
#         print(" ", end="\t")
#
#     for k in range(0, i):
#         print("*", end="\t")
#
#     print("\n")





#             *
#         *   *   *
#     *   *   *   *   *
# *   *   *   *   *   *   *

#             *
#         *       *
#     *       *       *
# *       *       *       *


# class Mobile:
#     def show_model(self):
#         print("realmex")
#

# class studets:
#     def __init__(self):
#         self.name = "purshottam"
#         self. age = 20
#         self.marks = 300
#
#     def talk(self):
#         print("my name is:",self.name)
#         print("my age is :",self.age)
#         print("my marks is:",self.marks)
#
# ram = studets()
# ram.talk()

# class studetns:
#     def __init__(self,n ="",m = 0):
#         self.name = n
#         self.marks = m
#
#     def display(self):
#         print("hi my name is :",self.name)
#         print("and i got the marks:",self.marks)
#
# s = studetns("purshottam",880)
# s.display()

# class studets:
#     def __init__(self,n ="",m = 0):
#         self.name = n
#         self.marks = m
#
#     def display(self):
#         print("my name is :",self.name)
#         print("my marks is :",self.marks)
#
#     def calculate(self):
#         if(self.marks>=600):
#             print("you got first prize:")
#         elif(self.marks>=500):
#             print("you got second grade:")
#         elif(self.marks>=350):
#             print("you got third grade:")
#         else:
#             print("you will be fail:")
#
#
# n = int(input("how many studetns : "))
# i = 0
# while (i<n):
#     name = input("enter your name:")
#     mark =int(input("enter your marks:"))
#
# s_1 = studets("name","mark")
# s_1.display()
# s_1.calculate()
# i+=1
# print("----")
#
#

# class employee:
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print("my id is:",self.id)
#         print("my name is :",self.name)
#         print("my salary is:",self.salary)
# class my_class:
#     @staticmethod
#     def my_method(a):
#         a.salary+=1000
#         a.display()
# ram = employee(20,"purshottam",30000)
# my_class.my_method(a)

# class my_class:
#     @staticmethod
#     def my_love(x,y):
#         result = x**y
#         print("{} to the power of {} is {}".format(x,y,result))

#my_class.my_love(5,4)


# class Father:
#     def __init(self):
#         self.property = 80000
#     def display_property(self):
#         print("Father property",self.property)
#
# class son("father"):
#     pass
# s = son()
# s.s

# class Father:
#     def __init__(self):
#         self.property = 80000
#         self.proprty_1 = 90000
#
#     def display(self):
#         print(self.property,self.proprty_1)
#
# class child(Father):
#     def __init(self):
#         self.property_2 = 90000
#         self.propert_3 = 20000
#
#     def display_2(self):
#         print(self.property_2,self.propert_3)

# object = child()
# object.display_2()
# object.display()

# class students:
#     def __init__(self):
#         self.name = "purshottam"
#         self.age = 28
#         self.marks = 90
#     def talk(self):
#         print("Hi my name is ",self.name)
#
# pooja = students()
# pooja.talk()

# class students:
#     def __init__(self,n="",m=0):
#         self.name=n
#         self.marks=m
#     def display(self):
#         print("Hi",self.name)
#         print("yours marks",self.marks)
#
# object = students("pooja Roy",500)
# object.display()


    # instance variable


# class students:
#     def __init__(self):
#         self.x = 50
#
#     def modify(self):
#         self.x+=1
#
# pooja=students()
# pooja2=students()
# print("x in pooja",pooja.x)
# print("x in pooja2",pooja2.x)
# pooja.modify()
# print("x in pooja",pooja.x)
# print("x in pooja2",pooja2.x)

# class papa:
#     nikita = 20
#     @classmethod
#     def modify(cls):
#         cls.nikita+=1
#
# anjali=papa()
# nikki= papa()
#
# print("nikita in anjali",anjali.nikita)
# print("nikita in nikki",nikki.nikita)
#
# anjali.modify()
# print("nikita in anjali",anjali.nikita)
# print("nikita in nikki",nikki.nikita)

#  student class with intance methods to process the data of several students:

# class students:
#     def __init__(self,n="",m=0):
#         self.name = n
#         self.marks =m
#
#     def display(self):
#         print("Hi my name is ",self.name)
#         print("your marks card is ",self.marks)
#
#     def calculate(self):
#         if(self.marks>=600):
#             print("you got it First grade")
#         elif(self.marks>=500):
#             print("you got it second grade")
#         elif(self.marks>=350):
#             print("you got it third Grade")
#         else:
#             print("you will be failed")
#
# pooja = int(input("How many students?"))
# i = 0
# while(i<pooja):
#     name =input("Enter your name:")
#     marks = int(input("Enter your marks:"))
#     sweety = students(name,marks)
#     sweety.display()
#     sweety.calculate()
#     i+=1

# accesor and mutator methods:

# class students:
#     def setname(self,name):
#         self.name = name
#     def getname(self):
#         return self.name
#
#     def setmarks(self,marks): mututor method
#         self.marks = marks
#     def getmarks(self): accessor method
#         return self.marks
#
# maa= int(input("how many Students:"))
#
# i=0
# while (i<maa):
#     s = students()
#     name = input("Enter your name:")
#     s.setname(name)
#     marks= int(input("Enter your marks:"))
#     s.setmarks(marks)
#     print("Hi",s.getname())
#     print("your marks is",s.getmarks())
#     i+=1

#  class method

# class bird:
#     wings = 2
#     @classmethod
#     def fly(cls,name):
#         print("{} flies with {} wings".format(name,cls.wings))
#
# bird.fly("sparrow")
# bird.fly("pigeon")

# square root

# import math
# class pooja:
#     @staticmethod
#     def calculator(x):
#         result = math.sqrt(x)
#         return result
# num =float(input("Enter your number:"))
# res = pooja.calculator(num)
# print("square root of {} is {: .3f}" .format(num,res))

# import sys
# class Bank(object):
#     """ Bank realted transcations"""
#
#     # to initialiasing name and balnce instance vars
#
#     def __init__(self,name,balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     # to add deposit amount to balance
#
#     def deposit(self,amount):
#         self.balance +=amount
#         return self.balance
#
#     # to deduct withdrwal amount from balance
#
#     def withdraw(self,amount):
#         if amount >self.balance:
#             print("balance amount is less,so no withdrwal")
#         else:
#             self.balance -=amount
#             return self.balance
#
# name = input("Enter your name: ")
# b=Bank(name)
#
# while(True):
#     print("d - deposit, w -withdraw,e-Exit")
#     choice = input("your choice:")
#     if choice =="e" or choice =="E":
#         sys.exit()
#     amt =float(input("Enter your amount:"))
#
#     if choice =="d" or choice =="E":
#         print("balance after deposit:",b.deposit(amt))
#     elif choice =="w" or choice == "W":
#         print("Balance after Withdrawl:",b.withdraw(amt))

# class myclass:
#     @staticmethod
#     def mymethod(x,n):
#         result= x**n
#         print(result)
#
# myclass.mymethod(5,3)

# class Person:
#     def __init__(self):
#         self.name = "purshottam"
#         self.db = self.Dob()
#     def display(self):
#         print("name",self.name)
#
# class Dob:
#     def __init__(self):
#         self.dd = 26
#         self.mm = 6
#         self.yy = 1995
#     def display(self):
#         print(self.dd,self.mm,self.yy)
#
# pooja = Person()
# pooja.display()
#
# nikki = pooja.db
# pooja.display()

# class myclass:
#     @staticmethod
#     def love(x,n):
#         result = (x**n)
#         print(result)
# myclass.love(5,3)

# class Person:
#     def __init__(self):
#         self.name = "Purshottam"
#
#     def display(self):
#         print("name = ",self.name)
#
# class Dob:
#     def __init(self):
#         self.dd = 26
#         self.mm = 7
#         self.yy =1995
#
#     def display(self):
#         print("Dob = ",self.dd,self.mm,self.yy)
#
#
# nikki = Person()
# nikki.display()
# anni = Person().Dob()
# anni.display()
#print(anni.yy)


# class Father:
#     def __init__(self):
#         self.property = 80000
#
#     def display(self):
#         print("father Property",self.property)
#
# class son(Father):
#     pass
# s = son()
# s.display()


# class father:
#     def __init__(self):
#         self.property = 80000
#
#     def display(self):
#         print("father Property",self.property)
#
# class Son(father):
#     def __int__(self):
#         self.property = 50000
#
#     def display2(self):
#         print("son Property",self.property)
#
# s = Son()
# s.display2()

# class Bank(object):
#     cash = 24000
#     @classmethod
#
#     def available_cash(cls):
#         print(cls.cash)
# class Andhrabank(Bank):
#     pass
#
# class State_Bank(Bank):
#     @classmethod
#
#     def available_cash(cls):
#         print(cls.cash+Bank.cash)
#
# A = Andhrabank()
# A.available_cash()
#
# b = State_Bank()
# b.available_cash()

# class myclass:
#     def calculate(self,x):
#         print("square value=",x*x)
#
# object = myclass()
# object.calculate(2)
#
# object_2 = myclass()
# object_2.calculate(3)



# a = open("myfile.text","w")
# puru = input("Enter your name : ")
#
# a.write(puru)
# a.close()

# a = open("myfile.text","r")
# puru = a.read()
#
# print(puru)


# print("hello ")



# class human:
#     def __init__(self,height,weight):
#         def read(self,read):
#             print(read)
#
#         def book(self,fund):
#             print(fund)
#
# object = human(50,60)
# object.read("book")
# object.book("amount")


# import time
# epoch = time.time()
# print(epoch)

# import time
#
# t = time.ctime()
# print(t)

# from datetime import *
#
# pooja = datetime.now()
# print(pooja)

# from datetime import *
#
# pooja = datetime.today()
# print("Today date it is : ",pooja)
#
# pooja_1 = date.today()
# print(pooja_1)

# from datetime import *
# pooja = date.today()
# print(pooja)
# nikki = pooja.strftime("%d,%b,%Y")
# print(nikki)

# from datetime import *
#
# pooja = date.today()
# print(pooja)
#
# sundari = pooja.strftime("%j")
#
# print("Today is ",sundari,"th day of the current year")
#
# sundari_1 = pooja.strftime("%A")
#
# print("it is ",sundari_1)

# from calendar import *
#
# yy = int(input("Enter year:"))
# mm = int(input("Enter the months:"))
#
# pooja = month(yy,mm)
# print(pooja)

# from calendar import *
#
# y = int(input("Enter the year:"))
#
# if(isleap(y)):
#     print(y,"is leap year")
# else:
#     print(y,"not a leap year")

# from calendar import *
#
# year = int(input("Enter the year : "))
#
# print(calendar(year,2,1,6,3))

# from calendar import *
#
# year = int(input("Enter the months"))
#
# print(calendar(year,2,1,6,3))


# import qrcode as qr
# img = qr.make("https://login.oracle.com/mysso/signon.jsp")
# img.save("purshottam_youtube.png")

# import time
# epoch = time.time()
# print(epoch)

# import time
#
# t = time.ctime()
# print(t)

# from datetime import *
#
# pooja = datetime.now()
# print(pooja)

# from datetime import *
#
# pooja = datetime.today()
# print("Today date it is : ",pooja)
#
# pooja_1 = date.today()
# print(pooja_1)

# from datetime import *
# pooja = date.today()
# print(pooja)
# nikki = pooja.strftime("%d,%b,%Y")
# print(nikki)

# from datetime import *
#
# pooja = date.today()
# print(pooja)
#
# sundari = pooja.strftime("%j")
#
# print("Today is ",sundari,"th day of the current year")
#
# sundari_1 = pooja.strftime("%A")
#
# print("it is ",sundari_1)

# from calendar import *
#
# yy = int(input("Enter year:"))
# mm = int(input("Enter the months:"))
#
# pooja = month(yy,mm)
# print(pooja)

# from calendar import *
#
# y = int(input("Enter the year:"))
#
# if(isleap(y)):
#     print(y,"is leap year")
# else:
#     print(y,"not a leap year")

# from calendar import *
#
# year = int(input("Enter the year : "))
#
# print(calendar(year,2,1,6,3))

# from calendar import *
#
# year = int(input("Enter the months"))
#
# print(calendar(year,2,1,6,3))


# import qrcode as qr
# img = qr.make("https://login.oracle.com/mysso/signon.jsp")
# img.save("purshottam_youtube.png")


# import time
# epoch = time.time()
# print(epoch)

# import time
#
# t = time.ctime()
# print(t)

# from datetime import *
#
# pooja = datetime.now()
# print(pooja)

# from datetime import *
#
# pooja = datetime.today()
# print("Today date it is : ",pooja)
#
# pooja_1 = date.today()
# print(pooja_1)

# from datetime import *
# pooja = date.today()
# print(pooja)
# nikki = pooja.strftime("%d,%b,%Y")
# print(nikki)

# from datetime import *
#
# pooja = date.today()
# print(pooja)
#
# sundari = pooja.strftime("%j")
#
# print("Today is ",sundari,"th day of the current year")
#
# sundari_1 = pooja.strftime("%A")
#
# print("it is ",sundari_1)

# from calendar import *
#
# yy = int(input("Enter year:"))
# mm = int(input("Enter the months:"))
#
# pooja = month(yy,mm)
# print(pooja)

# from calendar import *
#
# y = int(input("Enter the year:"))
#
# if(isleap(y)):
#     print(y,"is leap year")
# else:
#     print(y,"not a leap year")

# from calendar import *
#
# year = int(input("Enter the year : "))
#
# print(calendar(year,2,1,6,3))

# from calendar import *
#
# year = int(input("Enter the months"))
#
# print(calendar(year,2,1,6,3))


# import qrcode as qr
# img = qr.make("https://login.oracle.com/mysso/signon.jsp")
# img.save("purshottam_youtube.png")


 # file handling
# file handlig is a mechanism through which we can handle (create, read, append, delete) in the file

# file = open("filepath", "mode")
# open() is a fumction to work with file and it takse basically two argumentar
# fileMode:
# r=read
# w=write
# a=append
# r+ = both read & write
# b = binary mode


#
# file = open("C:\\Users\\purshottam kumar\\Desktop\\New folder\\a.xlsx", "w")
# file.write("pooja ")
# try:
#     file = open("C:\\Users\\purshottam kumar\\Desktop\\New folder\\a.txt", "r")
#     data = file.readlines()
#     print(data)
# except:
#     print("File does not exists")
#
# file = open("A.txt", "w")
# print("File created successfully.")

# a python program to create read charcters from a text file.

# A = open("myfile.text","r")
#
# pooja = A.read()
# print(pooja)
#
# A.close()
#
# A = open("myfile.text","r")
# print("my name is purshottam kumar raj")
# puru = A.read()
# print(puru)
# A.close()

# a=15
# b=10
# c=10
#
# print(a>b and a>c)

# def functionname(parameter):
#     // statement


# function(argument)

# function is a group of statement. which only excute when we call the function.

# there are two type of function
# 1. in built function
#     print(), uppercase(), max(), min()
#
# 2. user defined function

# def pooja():
#     print("Jai shree ram")
#     print("jai shri ganesh")
#
# pooja()

# parametrized function
# def sumoftwonumber(a, b, c):
#     print(a+b+c)
#
#
# sumoftwonumber(500,10, 20)
#
# x=5
# y=8
# z=x+y
# print(z)

# def sum(a,d):
#     b=5
#     c=a+b+d
#     print(c)
#
# sum(15,5)


# def sum(a, b):
#     c = a+b
#     return c
#
# d = sum(5,8)
# print(d)

# def subtract(x, y):
#     return x-y
#
# print(subtract(4, 8))


# def number():
#     a=5
#     b=10
#     c=a+b
#     return c
#
# x = number()
# y = x+10
# print(y)

# def manvi():
#     name= "i love my mom"
#     print("mummy is my jaan",name)
# manvi()

# name="purshottam"
# a=name.rstrip()
# print(a)

# def pooja():
#     name= "purshottam"
#     print ("welcome to name",name)
# pooja()

# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# sum=add()
# print(sum)

# nested function

# def pooja():
#     print("my name is pooja")
#
#
# def niiki():
#     print("my name is nikki")
#
#
# pooja()
# niiki()


      # passing a parameter()

# def pooja(nikki):
#     print("my name is pooja"+ni())
# def niiki():
#     return("my name is nikita")
# pooja(nikki)


 #function return into another function

# def pooja():
#     def nikki():
#         print("My name is nikki")
#
#     print("My name is pooja")
#     nikki()
#
# pooja()


#dictinories

# persons={"age":"21","rahul":"102","ram":"103"}
# #print("the person age is " + persons["age"])
# persons["ram"]=105
# print(persons)

#lists

#colors=["red","green","blue","yellow","pagal"]
# first_colors=colors[0]
# print(first_colors)
# last_colors=colors[-1]

#using loop
# for color in colors:
#     print(color)

#adding items in list
#colors.append("pagal")

# name=input("what is your name?")
# print("hello "+ name)
# age=input("how old are you?")
# age=int(age


# a=len(list)-1

# print(a)?



# for i in range(0, len(list)-1):
#     if(list[i] == "deepu"):
#         print("yes deepu is available on index ", i)

# def searchName(list, name):
#     a=len(list)-1
#     for i in range(a, 0, -1):
#         if (list[i] == name):
#             print(name, " is availble on index", i)
#
# list = ["ram", "shyam","gita","deepu","niki","anni","nikita"]
# searchName("name")

# list=["ram","ram","kutta","sohan"]
# a=len(list)-1
# for i in range(a,0,-1):
#     if(list[i] == "sohan"):
#         print("yes sohan it is available in index",i)

# list=["ram","ram","shyam","sohan"]

# def function(list,name):
#     a=len(list)-1
#     for i in range(a,0,-1):
#         if(list[i]==name):
#             print(name,"yes available on index",i)
#             function(list,name)



# a= 5/5.5
# b= 5*5.5
# print(a//b)

# # if(n%2!=0):f(n%2!=0):
#         print("weird")
#     elif(n%2==0) and (n>=2 and n<=6):
#         print("Not weird")
#     elif(n%2==0) and (n>=6 and n<=20):
#         print("weird")
#     elif (n%2==0) and n>20:
#         print("Not weird")


# a=int(input("enter the first age"))
# b=int(input("enter the second age"))
# c=int(input("enter the third age"))
#
# max=a
# if max<b:
#     max=b
# if max<c:
#     max=c
# print(max)

# temp=float(input("enter the temp in celcius"))
# fahrenheit=(temp * 1.8 )+32
# print(fahrenheit)


# a=int(input("enter the value of a"))
# b=int(input("enter the second value"))
# temp=a
# a=b
# b=temp
# print("enter the value of:",a)
# print("enter the value of :",b)

#print triangle

# a=int(input("enter your first angle"))
# b=int(input("enter your second angle"))
# c=int(input("enter your third angle"))
#
# if a+b+c==180 and a!=0 and b!=0 and c!=0:
#     print("possible")
# else:
#     print("not possible")

# there are 3 number print highest no

#swap two number

# a=int(input("enter the first digit"))
# b=int(input("enter the second digit"))
#
# temp=a
# a=b
# b=temp
#
# print("enter the first digit:",a)
# print("enter the second digit:",b)


#sum of 3 digit number

# num=int(input("enter your three digit number"))
# a=num % 5
# num=num//5
# b=num % 5
# c=num//5
#
# love=a+b+c
# print(love)

#checking the no even or odd

# x=int(input("enter your number"))
# if x % 2==0:
#     print("even")
# else:
#     print("odd")

#given year is leap year ya not

# year=int(input("enter your year"))
# if year % 4==0:
#     print("leap year")
# else:
#     print("not a leap year")

#profit and loss

# cp=float(input("enter your cost price"))
# sp=float(input("enter your selling price"))
#
# if cp >sp:
#     amount=cp-sp
#     print("loss:",amount)
# else:
#     amount=sp-cp
#     print("profit:",amount)

#simple interst

# p=int(input("enter your principle"))
# r=int(input("enter your rate of interest"))
# t=int(input("enter your time period in year"))
#
# simple_interst= (p*r*t)/100
# print("your simple interst is:",simple_interst)
#
# b= p+simple_interst
# print("enter your amount:",b)

# a=int(input("enter your number"))
#
# if a % 3==0 and a % 6==0:
#     print(a,"is divisible by 3 and 6")
# else:
#     print(a,"is divisible by 3 and 6")

#armstrong number

# love=int(input("enter your no:"))
# dhoka=love
#
# a=dhoka % 5
# dhoka=dhoka//5
# b=dhoka % 5
# c=dhoka//5
#
# if(a**3)+(b**3)+(c**3)==love:
#     print("armstrong number")
# else:
#     print("not a armstrong number")

# in hand salary calculation

# a= float(input("enter your annual salary"))
# if a > 500000 and a < 100000:
#     tax=(10/100)*a
#     b= a-tax
# elif a > 100000 and a< 2000000:
#     tax=(20/100)*a
#     b=a-tax
# else:
#     tax=(30/100)*a
#     b=a-tax
#
# print("after salary reduction :",b)
#
# HRA=(10/100)*b
# DA= (5/100)*b
# PF= (3/100)*b
#
# in_hand_salary=(b-HRA-DA-PF)/12
# print("in hand salary:",in_hand_salary)


#
# try:
#     file = open("e:\\self.txt", "r")
#     data = file.readlines()
#     print(data)
#     file2 = open("e:\\self_duplicate.txt", "w")
#     for d in data:
#         file2.write(d)
#
#     print("data copied successsfully")
# except:
#     print("file does not exist")




# try:
#     with open("e:\\self.txt", "r") as file:
#         with open("e:\\self_duplicate_copy.txt", "w") as file2:
#                 for d in file:
#                   file2.write(d)
#
#     print("data copied successsfully")
# except:
#     print("file does not exist")

# def sum ():
#     a = 5
#     b = 20
#     c = a + b
#     return c
# sum_1 = sum()
# print(sum_1)

# def number():
#     a = 5
#     b = 11
#     c= a+b
#     return c
# x = number()
# y = x + 10
# print(y)
#

# def sum():
#     num_1 = int(input("enter the first number: "))
#     num_2 = int(input("enter the second number: "))
#
#     sum_2 = num_1 + num_2
#
# print("sum_2")
#
# def sum_3(num_1,num_2):
#
#     sum = num_1 + num_2
#     print("sum")
#
# def sum_4(num_1,num_2):
#     sum_5 = num_1 + num_2
#
#     return(sum_5)
#
# sum()
# print("calling the first number : ")


# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c = int(input("enter the third number:"))
#
# if a > b :
#     if a > c :
#         print("big")
#     else:
#         if b > c:
#             print("less")
# else:
#     print("nothing")

# class human:
#     def __init__(self,height,weight):
#         print(height,weight)
#
#     def reaad(self,read):
#         print(read)
#
#     def wrritee (self,love):
#         print(love)
#
# object = human(50,60)
# object.reaad("read")
# object.wrritee("love")

# class person:
#     def __init__(self):
#         self.age = 30
#         self.height = 5.5
#         self.weight = 80
#
#     def show(self):
#         print(self.age,self.height,self.weight)
#
# object = person()
# object.show()

# class Nikki:
#     def __init__(self):
#         self.age = ""
#         self.height = ""
#         self.weight = ""
#
#     def set_data(self,age,height,weight):
#         self.age = 30
#         self.height = "5.5ft"
#         self.weight = "80kg"
#
#     def show_data(self):
#         print(f"{self.age},{self.height},{self.weight}")
#
# object = Nikki()
# object.set_data(50,"5.5ft","80kg")
# object.show_data()



# list = [10,5,90,30,20,7,8]
#
# print("before sorting " ,list)
#
# list.sort(reverse=True)
#
# print ("after the sorting",list)
#
# for love in list:
#    print(love)

# a= ["cc","bba","cbs","aaa","eee"]
# a.sort(key=len)

# sorting

# user_input = []
# for i in range(0,5):
#     num=int(input("enter the value "))
#     user_input.append(num)

# for i in range(0,len(user_input)-1):
#     min_value=min(user_input[i:])
#     min_index=user_input.index(min_value,i)
#     user_input[i],user_input[min_index]=user_input[min_index],user_input[i]
# print(user_input)

# list=[]
# for i in range(0, 5):
#     ele = int(input("Enter the value: "))
#     list.append(ele)
# for i in range(0, len(list)-1):
#     for j in range(i+1, len(list)):
#         if list[i]>list[j]:
#             temp = list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list)
# # print(list)

# list[]
# for i in range(0,5):
#     element=int(input("enter your value: "))
#     list.append(element)
#     for i in range(0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]> list[j]:
#                 temp=list[i]
#                 list[i]=list[j]
#                 list[j]=temp
# print(list)


# list=[]
# for i in range(0,5):
#     kia=int(input("enter your value "))
#     list.append(list)
#     for i in range(0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if [i]>list[j]:
#                 temp=list[i]
#                 list[i]=list[j]
#                 list[j]=temp
# print(list)

# class maa:
#     def __init__(self):
#         self.name = ""
#         self.age =""
#         self.address = ""
#     def set_date(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def show_data(self,):
#         print(f"{self.name},{self.age}.{self.address}")
#     object=maa()
#     object.set_date("purshottam",28,"gurpa")

# class human:
#     def __init__(self,height,weight):
#         print(height,weight)
#     def read(self,subject):
#         print(subject)
#     def write(self,good):
#         print(good)
#
# object=human(50,60)
# object.read("physcis")
# object.write("good")


# class person:
#     def __init__(self):
#         self.age = 28
#         self.weight=70
#         self.height="5.5ft"
#     def ram(self):
#         print(self.age,self.weight,self.height)
#
# object=person()
# object.ram()

# class p:
#     def __init__(self):
#         self.name=""
#         self.age=""
#         self.address=""
#     def set_data(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show_data(self):
#         print(f"{self.name},{self.age},{self.address}")
#
# object_p=p()
#
# object_p.set_data("purshottam",28,"koreya")
# object_p.show_data()


# class calculator:
#     def __init__(self,a,b):
#         self.x = a
#         self.y= b
#     def addition(self):
#         print(self.x + self.y)
#     def subtraction(self):
#         print(self.x - self.y)
#     def multiplication(self):
#         print(self.x * self.y)
#     def divide(self):
#         print(self.x % self.y)
#
# cal = calculator(8,4)
# cal.addition()
# cal.subtraction()
# cal.multiplication()
# cal.divide()

# class empoyeess:
#     def init__(self):
#         self.name = ""
#         self.address = ""
#         self.age = ""
#         self.salary=""
#         self.count=0
#         self.list=[]
#
#     def set_data(self,name,address,age,salary ):
#         self.name = name
#         self.address = address
#         self.age = age
#         self.salary = salary
#         self.count+=1
#         self.list.append({"name":name},{"address":address})
#
#     def show_data(self):
#         print(f"{self.name},{self.address},{self.age},{self.salary}")
#
# object = empoyeess()
# object.set_data("ram","koreya",30,30000)
# object.show_data()




# import calendar
# p=calendar.TextCalendar(calendar.TUESDAY)
#
# p.prmonth(2021,12)






# list = [23,54,67,89,34]
# list_1 = []
# for i in list:
#     list_1.append(list)
#     print(list_1)

# number = [4,5,8.9,45,-1,-5]
# number_1 = []
# for p in number:
#     square = p ** 2
#     number_1.append(square)
#     print(square)

# a = 10
# b= 20
# if a > b :
#     print("b is greater than a")
# else:
#     print("a is greter than b ")


# a = 10
# b = 20
# c = 30
#
# if a>b and a<c:
#     print("a is greatest ")
# elif b>a and b<c:
#     print("b is the greatest")
# else:
#     print("c is the gratest")

# i = 6
# while i<=10:
#     print(i)
#     i += 1

# i = 1
# n = 2
# while i <=10:
#     print(n ," * ",i," = ",n*i)
#     i+=1

# i = 1
# n = 2
# while i <=10:
#     print(n, " * ","i ","=",n*i)
#     i+=1

# list = [1,2,3,4,5,7,8,9,10]
# i = 0
# while i<len(list):
#     list[i] = list[i]+100
#     i+=1
#     print(list)

# i = 1
# n = 3
# while i<=20:
#     print(n," * ","i","=",n*i)
#     i+=1

# list = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i<len(list):
#     list[i] = list[i]+100
#     i+=1
#     print(list)

# def yarnex():
#     print("exhibition is mumbai")
# object = yarnex()
#

# def sum_add(x):
#     return(x+10)
# sum = sum_add(20)
# print(sum)

# def odd (x):
#     if x % 2 == 0:
#         print(x,"even number")
#     else:
#         print(x, "odd number")
# number = odd(5)

# class phone:
#     def make_call(self):
#         print("i am doing a call")
#     def play_game(self):
#         print("i will play game")
# my_love = phone()
# my_love.make_call()
# my_love.play_game()

# class phone:
#     def set_color(self,color):
#         self.color = color
#     def set_cost(self,cost):
#         self.cost = cost
#     def show_color(self):
#         print(self.cost)
#     def show_cost(self,cost):
#         print(self.cost)
#     def make_call(self):
#         print("i am calling it")
#     def play_game(self):
#         print("i will play videos game")
# ram = phone()
# ram.set_color("blue")
# ram.set_cost(5000)
# ram.show_color()
# ram.make_call()
# ram.play_game()


# class Phone:
#     __color = ""
#     __cost =  ""
#     def __init__(self):
#         pass
#     def set_color(self,color):
#         self.__color = color
#     def set_cost(self,cost):
#         self.__cost = cost
#     def show_color(self):
#         print(self.__color)
#     def show_cost(self):
#         print(self.__cost)
#
# pooja =Phone()
# pooja.set_color("blue")
# pooja.set_cost(5000)
# pooja.show_color()
# pooja.show_cost()
#


# class Phone:
#     def set_color(self):
#         print("my phone is black color")
#     def set_cost(self):
#         print("my phone cost")
#
# pooja = Phone()
# pooja.set_color()
# pooja.set_cost()

# class Phone:
#     def set_color(self,color):
#         self.color = color
#     def set_cost(self,cost):
#         self.cost = cost
#     def show_color(self,):
#         print(self.color)
#     def show_cost(self):
#         print(self.cost)
#
# pooja =Phone()
# pooja.set_color("blue")
# pooja.set_cost(5000)
# pooja.show_color()
# pooja.show_cost()
#

#
# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender
#
#     def show_employee_detail(self):
#         print("employee name is  ",self.name)
#         print("employee age is ",self.age)
#         print("employee salary is ",self.salary)
#         print("employee gender is ",self.gender)
#
# pooja = Employee("purshottam",28,50000,"male")
# pooja.show_employee_detail()

# class Human:
#     def __init__(self,height,weight):
#         print(height,weight)
#     def read(self,subject):
#         print(subject)
#     def laugh(self,health):
#         print(health)
# object =Human(170,70)
# object.read("physics")
# object.laugh("fine")
#
#
# class Human:
#     def __init__(self):
#         self.weight = 80
#         self.age = 29
#         self.height = "5.5ft"
#     def love(self):
#         print(self.weight,self.age,self.height)
#
# nikki = Human()
# nikki.love()

# class A:
#     def __init__(self):
#         self.name = ""
#         self.age = ""
#         self.height =""
#         self.weight =""
#     def set_data(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#     def show_data(self):
#         print(f"{self.name},{self.age},{self.height},{self.weight}")
#
# mast =A()
# mast.set_data("purshottam",29,"5.5ft","70kg")
# mast.show_data()

# list = [ 1,3,7,9,3,6,7,9,1]
#
# count = 0
# i = 0
# while i<len(list):
#     if list[i] == 9:
#         count+=1
#     i+=1
# print(count)

# list = [122,133,144,194,123]
#
# for i in list:
#     print(i)

# x = int(input("enter your number"))
# sum = 0
# for i in range(1,x+1):
#     sum =sum+i
#
# print(sum)


# x = int(input("enter the number"))
# sum = 0
# for i in range(1,x+1):
#     sum = sum+i
#
# print(sum)

# i = 1
# while i<5:
#     print(i)
#     i+=1

# for i in range(1,16):
#     print(i)
#     if i ==8:
#         break
#     else:
#         print("loop terminated easily")


# list = []
# for i in range (0,5):
#     y = int(input("enter your number"))
#     list.append(y)
#
#     for i in range(0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list[j] = temp
#
# print(list)


# persons = {"101": "rahul","202":"purshottam","303":"ram"}
# print(persons)
# persons["pooja"] = "501"
# print(persons)

# Ram = ["ram","shyam","mohan","kuku","sohan"]
# shyam = Ram[0]
# print(shyam)
#
# for pooja in Ram:
#     print(pooja)
#
# Ram.append("pagal")
# print(Ram)

# num = int(input("enter your number"))
# flag = True
# for i in range (2,num//2):
#     if num % i == 0:
#         flag = False
#         if(flag):
#             print("prime number")
#         else:
#             print("not prime number")

# n= int(input("enter the no rows"))
# k=1
# for i in range(0,n):
#     for j in range(1,i+2):
#         print("*", end =" ")
#     print("\n")

# p = int(input("enter the no rows "))
# s = 1
# for i in range (0,p):
#     for j in range(1,i+2):
#         print(i+1,end = " ")
#     print("\n")


# k = int(input("enter the no rows"))
# s = 1
# for i in range (0,k):
#     for j in range(1,i+2):
#         print("s", end =" ")
#         s+=1
#     print("\n")

# list =[]
# list_1 = [2,4,6,8,10,12,14,32]
# list_2 = [2,"harsh",3, "ram",5,"shyam"]
# list_3 = [[1,2],[2,4,6],[3,6,9,27]]
#
# print(f"{list},{list_1},{list_2},{list_3}")

# list_3 = [[1,2],[2,4,6],[3,6,9,27]]
# for i in list_3:
#     print("list\t",i)


# list_1 = [1,2,3,4,5]
# list_2 = [7,8,9,10,11]
#
# list_2.append(list_1)
# print(list_2)

# list_2.remove(10)
# print(list_2)
# list_2.insert(2,23)
# print(list_2)
#
# list_2.pop()
# print(list_2)

# name = input("enter the no element: ")
#
# pooja = 0
#
# for i in name:
#     pooja+=1
# print(pooja)

# a = int(input("enter the first input : "))
# b = int(input("enter the second input: "))
# c = int(input("enter the third input: :"))
#
# if a > b and a < c :
#     print("greatest")
# elif b > a and b < c:
#     print("lowest")
# else:
#     print("nothing")

# a = int(input("enter the first number : "))
# b = int(input("enter the second number:"))
#
# power = 1
# i = 1
# while i<=b :
#     power = power * a
#     i+=1

# name = input("enter your name: ")
# length = 0
# for i in name :
#     length = length +1
# print("lenth of the name ",length)


# for i in range (3):
#     for j in range (3):
#         print(i,j)

# class Mobile:
#     fp = "yes"
#     @staticmethod
#     def show_model():
#         print("fingerprint:",Mobile.fp)
#
# realme = Mobile()
# Mobile.show_model()


# list = [3,2,7,8,3,5,9,2,"purshottam ", "ram"]
# for i in list:
#     print(i)
#     if i == "purshottam":
#         print("yes")
#     else:
#         print("no")

# list = [3,4,8,2,1,6]
# squares = []
# for i in list:
#     square = i ** 2
#     squares.append(square)
# print(squares)

# count = 1
# while count<=10:
#     print(count)
#     count+=1
#     if count == 7:
#         break
#     print("hii")
# print("no")

# list = ["hi", "hello","welcome"]
# names = ["krishana","ram","purshottam"]
#
# for lists in list:
#     for name in names:
#         print(list,name)
#         if list == "hello" and name == "ram":
#             break
#         print("inner loop")
#     print("outer loop")




# keywords in python
#
# and, except, lambda, with
# as, finally, nonlocal, while,
# assert, False, None, yield,
# break, for, not, class, from,
# or, continue, global, pass,
# def, if, raise, del, import, return
# elif, in, true, else, is, try


# data type in python .

# python data type are used to define the data type of
# variable it defines whta type of we are going to stored
# numric- int float complex
# string - str
# sequence - list tuple
# binary - bytes bytarray, memoryview
# mapping- dict
# set - set
# None None



# c=(3+4j)
# int - 10,12,45
# float - 1.2, 5.6
# complex- (a+bi)
# print(type(c))

# string
# name="purushotam"
# name2="pooja"
# name3=name+" "+name2 #concatination
# print(f"my name is {name3}") # print using f string

# #slice operator :
# a=name[0:-1]
# print(a)

# my_list = [1,2,3,4,5,6,8,9,10]
# print(my_list[:2])

# ram = [2,7,8,9.2,5,8,2,1]
# print(ram[:3])

# operator in python
# 1. arithmetic operator
# 2. Relational operator
# 3. assignment operator.
# 4. logical operator
# 5. bitwise operator
# 6. membership
# 7. identity operator

# 1. arithmetic operator
# +,add
# - subtract
# * multiply
# /  divide
# % - module
# **  exponent
# // floor divison

# a=2
# b=9
# c=b//a
# print(c)

# a= 5
# b= 8
# c=b//a
# print(c)

# a=b=10
# c=a
# print(a)
# print(b)
# print(c)

# relation operator or comparison operator
# ==
# !=
# >
# <
# <=
# >=
#


# if a<=b:
#     print("yes")
# else:
#     print("No")

# if a<=b:
#     print("yes ")
# else:
#     print("no")

# name="pooja"
# name2="puja"
#
# a=10
# b=20
# # if else ladder
# if a<b:
#     if name==name2:
#         print("Correct")
#     elif a>b :
#         print("yes a is greater than b")
#     else:
#         print("No a is not greater than b")
# else:
#     print("No")

# x=10
# y=10
# print(f"this condition is {x==y}") #truevv
# print(x>=y) #true


# 3. Assignment operator
# = equal assignment  a=10
# += addition assignment a+=10    (a=a+10)
# -= subtraction         a-=10    (a=a-10)
# *=                      a*=10   (a=a*10)
# /=                      a/=10   (a=a/10)
# %=                      a%=10   (a=a%10)
# **= exponent assignment a**=10  (a=a^10)
# //= floor division assignment   a//=10 (a=a//10)

# a=8
# b=-2
# print(b)
# b-=a
#
# print(b)

# 4. logical operator
# and or not
#
# and=> true = true = true
# or=> true = false = true
#
# not => true=false , false=true

# number1=input("Enter a number:")
# # input method always take string value
# number2=input("Enter 2nd number:")
# # type casting in python int(string value)
# sum=int(number1)+int(number2)
# print(sum)

# num=int(input("Enter a number:"))
# rem=num%2
# if rem==0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")


# a=50
# b=80
# c=30
#
# if a>b and a>c:
#     print(f"{a} is largest number")
# elif b>c and b>a:
#     print(f"{b} is largest number")
# else:
#     print(f"{c} is largest number")

# a=10
# b=10
# c=30

# if a>b or b>c:
#     print("True")
# else:
#     print("False")


# if not a==b:
#     print("true")
# else:
#     print("false")

# 8
#
#                              27        2^6   2^5   2^4   2^3   2^2   2^1   2^0
#                              128       64      32       16      8   4   2   1
# 1000
# 12 = 1100
# 15 = 1111
# 18 = 10010
# 5 = 101
# 250 =

# 5. bitwise operator
# & and
# | or
# ^ xor
# ~ one complement
# << left shift
# >> right shift

# 0=false
# 1=true

# x=16
# y=8
#
#
# print(x&y)

# # 2. or
# true+false=true
# false+true=true
# true+true=true
# fals+false=false
# x=8
# y=4
# 1 0 0 0
# 0 1 0 0
# 1 1 0 0
# print(x|y)

# 3. XOR ^

# true + true = false
# true + false = true
# false + true = true
# false + false = false

# x=8
# y=2
# 1 0 0 0
# 0 0 1 0
# print(x^y)

# ~ one complement / not
# true = false
# false = true

# x=-8
# x=12
# # 1 1 0 0 0 0
# print(x<<2)
#
# x=12
# # 0 0 1 1
# print(x>>2)


# print("Hello World")


# list = [1,4,6,3,9,8,5,3,6,2,5,3,9,2,1,1]
#
# counter = 0
# i = 0
# for i in range(0,len(list)-1):
#     if list[i] == 4:
#         counter+=1
#     i+=1
# print(counter)

# y = [7, 4, -9, -5, 4, -6, -8, 2, 1, 0, 0, 0, ]
#
# for i in range(0,len(y)-1):
#     for j in range (i+1,len(y)):
#         if (y[i]>y[j]):
#             temp = y[i]
#             y[i] = y[j]
#             y[j] = temp
# print(y)


# str = "pur usho tam puja"
#
# str_2 =""
# for i in range(0,len(str)):
#     if (str[i]==""):
#         pass
#     else:
#         str_2+= str[i]
# print(str_2)

# class human:
#     def __init__(self ,height, weight):
#         print(height,weight)
#
#     def read(self,maths,physics):
#         print(maths,physics)
#
#     def write(self,google,microsoft):
#         print(google,microsoft)
#
# pooja=human("5.5ft","80kg")
# pooja.read("good","bad")
# pooja.write("not good","not good microsoft")

# class Person:
#     def __init__(self):
#         self.name = "purshottam"
#         self.age = "28"
#         self.height = "5.5ft"
#
#     def show(self):
#         print(self.name,self.age,self.height)
#
# ram = Person()
# r



# if 5>2:
#     print("greater")
#     print("5 is greater than 2")
# if (6>2):
#     print("6 is greater than two")
# print("rest of code")



# a= int(input("Enter number greater than 2:"))
#
# if (a>=2):
#     print("correct","you have Enterd:",a)
# else:
#     print("wrong","you have Enterd:",a)

a=5
b=2
c=6
d=3

# if(a>b):
#     print("a is greater than b:")
#     if(6>2):
#         print("c is greater than d")
#     else:
#
#      print("d is gretaer than c")
#
# else:
#     print("b is greater than a ")
#
# print("rest of code")

# list = [1,2,3,4,5]
# list_2 = [2,3,4,5,6]


# list_2.append(list)
# print(list_2)

#list = [1,2,3,4,5,6,6,5,4,3,2,1]
# list_2 =[]
# for i in list:
#     if i not in list_2:
#         list_2.append(i)
#     print(list_2)
# list_2 = max(list)
# print(list_2)
# list.reverse()
# print(list)
# ram = int(input("enter your number : "))
# for p in list:
#     if p ==ram:
#         print("True")
#         break
#     else:
#         print("False")

# i = 1
# n = 4
# while i<=20:
#     print(n,"*","i","=",n*i)
#     i+=1

# list = [1,4,2,6,2,3,8,7,9]
#
# for i in range(0,len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list)

# class Father():
#     def land(self):
#         print("10 bigha")
#
# class son(Father):
#     def money(self):
#         print("1 acres")
#
# ram = son()
# ram.money()
# ram.land()

# class A:
#     x = 10
#     y = 20
#     def addition(self):
#         print(self.x - self.y)
# class B(A):
#     def subtraction(self):
#         print(self.x-self.y)
#
#
# ram =B()
# print(ram.subtraction())
# print(ram.addition())

# class ram():
#     first_name = "laxman"
#     second_name = "satru"
#     third_name = "sita"
#     def display(self):
#         print(self.first_name+" ",self.second_name+" ",self.third_name+" ")
#
# class laxman():
#     first_name = "nikki"
#     second_name = "ram"
#     third_name = "mahrhu"
#     def display_1(self):
#         print(self.first_name+" ",self.second_name+"",self.third_name)
#
# class Sita(ram,laxman):
#     first_name = "chotu"
#     second_name = "babu"
#     third_name = "lotu"
#     def display_2(self):
#         print(self.first_name+"",self.second_name+"",self.third_name)
#
# object = Sita()
# object.display_2()
# object.display_1()
# object.display()
#
# class Father():
#     def land(self):
#         print("50 bigha")
#
# class son(Father):
#     def plot(self):
#         print("10 bigha")
# class son_1(Father):
#     def plot_1(self):
#         print("30 bigha")
#
# class son_2(Father):
#     def plot_2(self):
#         print("40 bigha")
#
# ram = son()
# ram.plot()
# ram_1 = son_1()
# ram_1.plot_1()


# a = int(input("Enter your first digit number:"))
# b = int(input("Enter your second digit number:"))
# c = int(input("Enter your third digit number:"))
#
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
#
# print(max)

# a = int(input("Enter your First number:"))
# b = int(input("Enter your second number"))
#
# max = a
#
# a = b
#
# b = max
# print("Enter your first number",a)
# print("Enter your second number",b)

# a = int(input("Enter your even number:"))
# if a % 2 ==0:
#     print("even")
# else:
#     print("odd")

# from datetime import *
# puru = datetime.today()
# print(puru)

# Python program to get Current Time

# from datetime import *
# puru = datetime.now()

# print(puru)

# puru = datetime.today()
# print(puru)
# pooja = puru.strftime("%D,%B,%Y")
# print(pooja)


# from datetime import *
# puru = date.today()
# print(puru)
# pooja = puru.strftime("%j")
# print(pooja)
# nikita = puru.strftime("%A")
# print(nikita)

# from calendar import *
# puru = int(input("Enter Your Year"))
# if(isleap(puru)):
#     print("yes it is leap year")
# else:
#     print("no it is no leap year")

# pooja = int(input("Enter your Year ! "))
# if(pooja %4 == 0):
#     print("leap year")
# else:
#     print("no leap Year")

# import pandas as pd
#
# ram = pd.read_excel("H:\\downloads\\Session-1practiceanddiscussion(1)")
# print(ram)

#  import pandas as pd
# # # pooja = pd.read_excel("H:\\downloads\\Session-1practiceanddiscussion (1)")
# # # print(pooj

# FIND THE LARGEST AMONG THREE NUMBERS :

# a=int(input("enter the first numbers :"))
# b=int(input("enter the second numbers: "))
# c=int(input("enter the third numbers: "))
#
# max = a
# if max < b :
#     max=b
# if max < c:
#     max = c
#
# print(max)

# x= int(input("Enter the first numbers:"))
# y= int(input("Enter the second number:"))
# z= int(input("Enter the third number:"))
#
# max = x
# if max < y:
#     max=y
# if max < z:
#     max=z
# print(max)





# SWAP THE TWO VARIABLES :

# a=int(input("enter the first numbers"))
# b=int(input("enter the second numbers"))
# max = a
# a = b
# b = max
#
# print("enter the value of a " ,a )
# print ("enter the value of b " ,b)

# x= int(input("Enter the first number:"))
# y= int(input("Enter the second number:"))
#
# max = x
# x = y
# y = max
#
# print("enter the value of x",x)
# print("enter the value of y",y)

#  ADD THREE DIGIT NUMBER BY TAKING INPUT FROM USER :

# num =int(input("enter the three digit number"))
# a= num % 10   # (345%10=5)
# num = num//10 #  (345//10=34)
# b = num % 10    # (34//10=4)
# c = num // 10    # (34//10=3)
#
# love=(a+b+c)
# print(love)


# CHECK IF THE NO IS EVEN OR ODD

# a= int(input("enter your number"))
# if a % 2 ==0:
#     print("even")
# else:
#     print("odd")

# LEAP YEAR

# year =int(input("enter your year"))
# if year % 4==0:
#     print("leap year")
# else:
#     print("not leap year")


# year =int(input("enter your year"))
# if year % 4==0:
#     print("leap year")
# else:
#     print("not leap year")

# TO CALCULATE PROFIT AND LOSS FOR GIVEN SELLING AND COST PRICE :

# cp = float(input("enter your cost price"))
# sp = float(input("enter your selling price"))
#
# if cp>sp:
#     amount = cp-sp
#     print("loss",amount)
# else:
#     amount = sp-cp
#     print("profit",amount)

# CALCULATE THE SIMPLE INTEREST

# p = int(input("enter principle amount"))
# r = int(input("enter the rate of interst"))
# t = int(input("enter your time period in year"))
#
# simple_intest = (p * r * t)/100
# print("your si interst",simple_intest)
#
# a = p * simple_intest
# print("your total amount is " ,a )

# GIVEN NO IS DIVISIBLE BY BOTH 3 & 6

# num = int(input("enter your no"))
# if num % 3 ==0 and num % 6==0:
#     print(num,"is divisible by 3 & 6 ")
# else:
#     print(num,"not divisible by 3 and 6 ")

#  ENTER THE FIRST NTH NUMBER:

# x = int(input("enter your number"))
# s = x * (x+1)/2
# print(s)

# MULTIPLY TWO NUMBER WITHOUT USING * OPERTATOR

# first_number = int(input("enter your first_number: "))
# second_number = int(input("enter your second number"))
#
# sum = 0
#
# for i in range(0,first_number):
#     sum = sum + second_number
#     print("your result is sum : ",sum)
#

# PRINT FIRST 25 ODD NUMBER:

# x = int(input("enter your first number"))
# y = int(input("enter your second number"))
#
# for i in range(x,y+1):
#     if i % 2 !=0:
#         print(i)

# PRINT EVEN NUMBER :

# for i in range(0,50):
#     if i % 2 == 0:
#         print(i)

# i = 2
# while i<=50:
#     print(i)
#     i+=1

# TO CHECK THE NUMBER ARE PRIME OR NOT

# num = int(input("enter your "))
# flag = True
# for i in range(2,num//2):
#     if num % i ==0:
#         flag = False
#     if(flag):
#         print("prime number")
#     else:
#         print("not prime number")


# calculation of population

# flag = 0
# a = 10000
# print(a)
#
# while True:
#     b = (a)+((10*a)/100)
#     a = b
#     print(int(b))
#     flag = flag+1
#     if flag==9:
#         break

# find the factors of a given number :

# num = int(input("enter your number"))
# for i in range (1,num+1):
#     if num % i ==0:
#         print(i)


# find the length of string without using len :

# a = input("enter your sring")
# count = 0
# for i in a:
#     count+=1
# print(count)

# how to remove dupicate element list

# list = [1,2,3,31,5,6,8,9,4,7,8]
# list_1 = []
# for i in list:
#     if i not in list_1:
#         list_1.append(i)
# print(list_1)


# extract max value in list :

# list = [2,3,4,5,6,7,8,9,10]
#
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)


# reverse a given list :

# list = [2,3,6,9,5,3,6,9,]
# reverse = []
# for i in range(len(list)-1):
#     reverse.append(list[i])
# print(reverse)

# search a number in list

# list = [1,2,3,4,5,6,7,8,9,10]
# num = int(input("enter the number "))
# for i in list:
#     if i==num:
#         print("true")
#         break
#     else:
#         print("false")

# list of number in squqare

# l = [2,3,4,5,6,8,7,9]
# l1 = []
# for i in l:
#     l1.append(i*2)
#     print(l1)

# how to reverse word in string

# even and odd elements of a elements of a list in two differnt list using python:

# list = [1,2,3,4,5,6,7,8,9,10]
#
# even = []
# odd  = []
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("even")
# print("odd")

# i = "string"
# print("the value of i is ",i )
# t =type(i)

# name = input("enter your name\: ")
# print("Hi",name)

# num = int(input("enter the marks :"))
# if num > 40:
#     print("pass")
# else:
#     print("fail")

# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# c = int(input("enter the third number:"))
#
# max = a
#
# if max < b :
#     max = b
# if max < c:
#     max = c
# print(max)
#
# a = 5
# b = 7
# c = 8

# if a > b:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(c)
#     else:
#         print(b)

a = 20
b = 30
c = 40

# if a>b:
#     if b>c:
#         print(a)
#     else:
#         print(b)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(a)


# a = int(input("enter the first number\:"))
# b = int(input("enter the second number\:"))
# c = int(input("enter the third number\:"))
#
# if a>b:
#     if b>c:
#         print(a)
#     else:
#         print(b)
#     if b>c:
#         print(b)
#     else:
#         print(a)

# n = int(input("enter your number"))
#
# sum = n * (n+1)/2
# print(sum)

# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
#
# power = 1
# i = 1
#
# while i<=b:
#     power = power*a
#     i+=1
# print(power)

# a= int(input("enter your number"))
#
# p = 1
#
# for i in range(0,a):
#     for j in range(1,i+1):
#         print("*", end="" )
#         print()


# class human():
#     def __init__(self,height,weight):
#         print(height,weight)
#
#     def good(self,health):
#         print(health)
#
#     def laugh(self,wealth):
#         print(wealth)
#
# object = human("5.5 ft",80)
# object.good("ram")
# object.laugh("not good")

# class human:
#     def __init__(self):
#         self.age = 28
#         self.weight = 70
#         self.smart = "very smart"
#         self.health = "good health"
#
#     def show(self):
#         print(self.age, self.weight,self.smart,self.health)
#
# object = human()
# object.show()

# class maa:
#     def __init__(self):
#         self.mummy = ""
#         self.papa = ""
#         self.brother = ""
#         self. sister = ""
#
#     def set_data(self,mummy,papa,brother,sister):
#         self.mummy = mummy
#         self.papa =  papa
#         self.brother = brother
#         self.sister = sister
#
#     def show_data(self):
#         print(self.mummy ,self.papa ,self.brother,self.sister)
#
# object =maa()
# object.set_data("neelam" , "subhash","chotu","soni")
# object.show_data()

# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def addation(self):
#         print(self.a + self.b)
#
#     def subtraction(self):
#         print(self.a - self.b)
#
#     def multiplication(self):
#         print(self.a * self.b)
#
#     def division(self):
#         print(self.a % self.b)
#
# object = calculator(7,9)
# object.addation()
# object.subtraction()
# object.multiplication()
# object.multiplication()

# list = [7,8,9,1,2,3,4,5,8,4]
# list_2 = [3,5,7,8,3,2,4,7,8,9]
#
# for i in list_2:
#     list_2.append(i)
# print(list)

#list_1 = [1,2,4,5,7,8,9,2,4,5]
#list_2 = [5,7,8,2,3,5,9,2,4,8]

# num = int(input("enter your number: "))
# flag = True
# for i in range(2,num//2):
#     if num % i == 0:
#         flag = False
#         if(flag):
#             print("prime number")
#         else:
#             print("not prime number")
#
# list = [ 1,2,3,4 ,5 ,6]
#
# print(list[2:4])

# num = int(input("enter your number: "))
# flag = True
# for i in range(2,num//2):
#     if num % i == 0:
#         flag = False
#         if(flag):
#             print("prime number")
#
#         else:
#             print("not a prime number")

#
# # i = 1
# # n = 3
# # while i<=30:
# #     print(n, "*", "i","=",n*i)
# #     i+=1

# list = [1,2,3,4,5,6]
# list_2 = [2,3,4,5,6,7]
#
# for i in list_2:
#     list.append(i)
#     print(list)

# list=[2,3,45,6]
#
# list_2 = max(list)
# print(list_2)

# list = [4,5,7,9,2,4,9]
# list_2 = []
# for i in list:
#     list_2.append(i*2)
#
# print(list_2)

# list = [1,2,3,4,5,6,7,8,9,10]
# even = []
# odd  = []
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# list = [1,2,3,4,5]
# list_2 = [2,3,4,5,6]
# list_3 =[]
# for i in list:
#     list_3.append(i)
# for j in list_3:
#     list_3.append(j)
# print(list)

# list = [-7,-8,-4,2,3,4,8,1,2,4,9,10]
#
# for i in range(0,len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i] > list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp

print(list)

# list = [1,3,3,8,5,2,3,2,2,1,1,7,9,8]
#
# count = 0
# i = 0
# while i<len(list):
#     if list[i] == 8:
#         count+=1
#         i+=1
# print(count)


# Display a digit into word

# num = 1
# if num ==1:
#     print("one")

# DISPLAY A GROUP OF MESSAGE IF CONDITION ARE TRUE:

# puru = "yes"
# if puru == "yes":
#     print("yes")
#     print("this is what you said it ")

# given number is between 1 and 10

# x = int(input("enter your number :"))
# if x>=1 and x<=10:
#     print(x,"which is between 1 and 10 ")
# else:
   # print(x,"print which is below ")

# TO know the given number zero ,positive,negative

# num = -5
# if num ==0:
#     print(num,"is zeros")
# elif num>0:
#     print(num,"is positive")
# else:
#     print(num,"is negative")

# x= 1
# while x<=10:
#     print(x)
#     x+=1
# print("end")

# display even number between 100 and 200

# x =100
# while x>=100 and x<=200:
#     print(x)
#     x+=2
# print("end")

# to display even numbers between m and n

# m,n = [int(i) for i in input()]

# ram = "hello"
# for n in ram:
#     print(n)

# dispay odd number between 1 t0 50

# for i in range(1,50,2):
#     print(i)

# to display in decending order :

# for i in range(10,0,-1):
#     print(i)


# list = [10,20,30,"ram","shyam"]
# for i in list:
#     print(i)
#

# list = [20,30,40,50,60,70]
# sum = 0
# for element in list:
#     print(element)
#     sum+=element
# print("sum",sum)

# list = [20,30,40,50,60]
#
# sum = 0
# i = 0
# while i<len(list):
#     print(list[i])
#     sum+= list[i]
#     i+=1
# print(sum)


# list = [2,3,4,5,6,7,8,9,10]
#
# sum = 0
#
# for i in list:
#     print(i)
#     sum+=i
# print("sum of number :",sum)

# for x in range(1,11):
#     for y in range(1,11):
#         print("{:8}".format(x*y),end = "")
#     print()



# searching for an element in a list :

# list = [1,2,3,4,5,6,7,8,9,10]
# search = int(input("enter the element to search: "))
# for pooja in list:
#     if pooja == search:
#         print("enter the element found list : ")
#         break
# else:
#     print("enter the element not found list : ")

# x = 50
# while x>=1:
#     print("pooja",x)
#     x-=1
#     if x==10:
#         break
# print("out of loop")

# x = 0
# while x<10:
#     x+=1
#     if x>5:
#         continue
#     print(x)

# for i in range (1,10):
#     print(i)
#     if i==5:
#         break
#     else:
#         print("breaking ")
#

# x = 20
# while x>=1:
#     print("love",x)
#     x-=1
#     if x==5:
#         break
#     else:
#print("out")

# x = 0
# while x > 20:
#     x+=1
#     if x>10:
#         continue
#     print("mast",x)
# print("out of loop")

# list = [4,5,6,-2,-5,-9,1,-8,-3]
# for i in list:
#     if(i>0):
#         pass
#     else:
#         print(i)

# max = int(input("enter your prime number: "))
# for i in range(2,max+1):
#     for j in range(2,i):
#         if (i%j)==0:
#             break
#     else:
#         print(i)
#

# max = int(input("eneter your number : "))
# for i in range(2,max+1):
#     for j in range(2,i):
#         if(i%j)==0:
#             break
#     else:
#         print(i)
#

# for i in range(1,15):
#     print(i)
#     if i==10:
#         break
#     else:
#         print("breaking")
#

# x = int(input("Enter your Number"))
# if x%2==0:
#     print("even")
# else:
#     print("odd")

# for i in range(1,15):
#     print(i)
#     if i==10:
#         break
# else:
#     print("love")

# A = int(input("Enter your name:"))
# sum = 0
# for i in range(1,A+1):
#     sum = sum+i
# print(sum)

# i = 0
# while i<10:
#     print(i)
#     i+=1

# list =[1,3,5,9,2,9,1,5,6,9,10]
# count = 0
# i = 0
# while i<len(list)-1:
#     if list[i]==7:
#         count+=1
#         i+=1
#         print(count)

# x = int(input("Enter your name:"))
# if x%2==0:
#     print("even")
# else:
#     print("odd")
#
# # class A:
# #     a = 10
# #     b = 20
# #     def show(self):
# #         print(self.a + self.b)
# #
# # class B(A):
# #     def display(self):
# #         print(self.a - self.b)

# for i in range (1,15):
#     print(i)
#     if i==10:
#         break
# else:
#     print("breaking")

# x = int(input("Enter sum of Number:"))
# sum = 0
# for i in range(1,x+1):
#     sum = sum+i
#print(sum)

# i = 0
# while i<5:
#     print(i)
#     i+=1
#

#list = [10,20,30,40,50]

# i = 0
# while i<len(list):
#     print(list[i])
#     i+=1
#
# for i in list:
#     print(i)

# days = ["sunday","monday","Tuesday","Wednesday","thursday"]
#
# i=len(days)-1
# while i>0:
#     print(days[i])
#     i-=1

#list = [10,20,30,40,50]

# number = len(list)
# print(number)

# list.append(60)
# print("number after appending",list)

# list.insert(0,5)
# print(list)

# list.count

# print(list)

# x = []
#y = int(input("Enter"))


# list =[]
# for i in range(0,5):
#     y = int(input("Enter your number:"))
#     list.append(y)
#     for i in range (0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list[j] = temp
#
# print(list)






# list = [ 5,2,3,6,4,7]
#
# for i in range(0,len(list)):
#     for i in range(0,len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list[j] = temp
#
# print(list)


# y = [7,4,-9,-5,4,-6,-8]
#
# for i in range(0,len(y)):
#     for j in range(0,len(y)-1):
#         for k in range(i+1,len(y)):
#             if y[j]>y[k]:
#                 pooja = y[j]
#                 y[j] = y[k]
#                 y[k] = pooja
# print(y)

# list_1 = [2,3,6,9,8,10]
# list_2 = [4,8,9,2,7,9,1]
#
# for i in list_2:
#     list_1.append(i)
# print(list_1)

# nikki = ["anni","nikki","nikita","sweety""pooja"]
# nikka = ["purshottam","anni","pooja","ram","shyam"]
#
# list_1 = set(nikki)
# list_2 = set(nikka)
# list_3 = list_1.intersection(list_2)
# love = list(list_3)
# print(love)

# emp = []
#
# p = int(input("How many Employess?"))



# def swaplist(newlist):
#     size = len(newlist)
#     temp = newlist[0]
#     newlist[0] = newlist[size-1]
#     newlist[size-1] = temp
#     return newlist
# newlist = [12,35,9,35,24]
# print(swaplist(newlist))


# x = [1,2,3,4,5]
# y = [2,3,4,5,6,]
#
# temp = x
# x = y
# y = temp
#
# print("Enter the value",x)
# print("Enter the second value",y)

# a = 10
# b = 20
#
# x = max(a,b)
# print(x)


# import pandas as pd
# l = [1,2,3,4,5,6,7,8,9,10]
#
# pooja = pd.Series(l)
# print(pooja)


# import pywhatkit
#
# pywhatkit.sendwhatmsg("+918904475485", "Hello world",17,9)
#

# import qrcode as qr
# img =qr.make("https://www.youtube.com/watch?v=3KXZduvOfDo&list=RD3KXZduvOfDo&start_radio=1")
#
# img.save("purshottam.png")

# import phonenumbers
# from phonenumbers import timezone,geocoder,carrier
# number = input("Enter your no. with +91: ")
# phone = phonenumbers.parse(number)
# time = timezone.time_zones_for_number(phone)
# carrier = carrier.name_for_number(phone,"en")
# reg = geocoder.description_for_number(phone,"en")
# print(phone)
# print(time)
# print(carrier)
# print(reg)

# from instabot import Bot
# bot = Bot()
# bot.login(username="purshottam7425",password="     ")
# bot.upload_photo("IMG-20220607-WA0005.jpg",caption ="cute")
#bot.send_message("i love python","username")

# import smtplib as P
# object = P.SMTP("smtp.gmail.com",587)





























































































x = [3,5,6,2,1,3,0,4,2]
n = len(x)













