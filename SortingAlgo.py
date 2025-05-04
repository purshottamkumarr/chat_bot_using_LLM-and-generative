# Bubble sort
#x = [2,5,1,7,8,9,10]

# n = len(x)
# for i in range(0,n-1):
# #     for j in range(0,n-i-1):
# #         if x[j]>=x[j+1]:
# #             x[j],x[j+1] = x[j+1],x[j]
# # print(x)

# selection  sort

# for i in range(0, n-1):
#     small = i
#     for j in range(i+1, n):
#      if x[j] < x[small]:
#          small = j
#      x[i], x[small] = x[small], x[i]
#
# print(x)
#

# z = [8,6,5,3,2,4,1]
# n = len(z)
# for i in range(1,n):
#     key = z[i]
#     j=i-1
#     while j>=0 and key<z[j]:
#         z[j+1] = z[j]
#         j-=1
#     z[j+1]=key
#
# print(z)

# def sum(x, y):
#     a = x
#     b = y
#     print(a+b)
#
#
# sum(80, 60)

# def multiply(x,y):
#     a = x
#     b = y
#     print(a*b)
# multiply(22,24)
#
# def purshottam(count, value):
#     for i in range(1, count):
#         print(value)
#
# purshottam(10, "Ram")

# def bubble_sort(list):
#     n = len(list)
#     for i in range(0,n-1):
#         for j in range(0,n-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     print(list)
# l1 = [7,8,9,3,6,1,3,6,7]
# bubble_sort(l1)

# def factorail(value):
#     m = 1
#     for i in range(1,value+1):
#         m = m * i
#     print(m)
# factorail(23)

# def printPattern(number):
#     for i in range(0,number):
#         for j in range(0, i):
#             print("*", end=" ")
#         print()
#
# printPattern(10)

# list = [4,5,6,7,9,3,2,3,45,63,12,74]
# value = 9
# position=-1
# n=len(list)
#
# for i in range(0, n):
#     if list[i] == value:
#         position=i+1
#
# if position>0:
#     print("value is availble on position-", position)
# else:
#     print("value is not available ")

# List = [2, 8, 1, 4, 6, 3, 7, 10, 9, 0]
# n = len(List)
# value = 11
# position = -1
#
# for i in range(0, n):
#     if List[i] == value:
#         position+= 1
# if position>0:
#     print("The Value is available",position)
# else:
#     print("The value is not available")














