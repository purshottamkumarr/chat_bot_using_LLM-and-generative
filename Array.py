# Array == list
# list = [1, 2, 3, 4, 5, 6]
#
# for i in list:
#     print(i)

# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# for i in range(len(list)):
#     if i == 4:
#         print(i)



# data = ["pooja", "karan", "puruttam", "Deepu", "arjun", "sanni"]
# print(data)
# i = 0
# while i <len(data):
#     if data[i] == "puruttam":
#         break
#     i+=1
#
# data[i] = "Purushottam"
#
# print(data)

# array -
# fixed size
# same data type

# data1 = "karan"
# data2 = "arjun"

# temp1 = data1
# data1 = data2
# data2 = temp1
# print("data1 - ",data1)
# print("data2 - ", data2)

# data1, data2 = data2, data1
# print("data1 - ",data1)
# print("data2 - ", data2)

# data1 , data2, data3 = "a", "b", "c"
#
# print(data1, data2, data3)

# data = ["pooja", "karan", "puruttam", "Deepu", "arjun", "sanni"]
# iok=-1
# ioj=-1
#
# i = 0
# while i < len(data):
#     if data[i] == "karan":
#         iok = i
#     if data[i] == "arjun":
#         ioj = i
#     i += 1
#
# print(iok, ioj)
#
# temp=data[iok]
# data[iok]=data[ioj]
# data[ioj]=temp

# print(data)

# data = ["pooja", "karan", "puruttam", "Deepu", "arjun", "sanni"]
# i = data.index("karan")
# j = data.index("arjun")
# data[i], data[j] = data[j], data[i]
# print(data)

# 2d array & sub array

# list = [4, 9, 6, 8, 2]
# 2^n - 1
# n * (n + 1) / 2

# 32 -1
# 31
# 4
# 4, 9
# 4, 9, 6
# 4, 9, 6, 8
# 4, 9, 6, 8, 2
# 9
# 9, 6
# 9, 6, 8
# 9, 6, 8, 2
# 6
# 6, 8
# 6, 8, 2
# 8
# 8, 2
# 2

List = [5, 8, 6, 3, 4, 8]

# 5
# 5,8
# 5,8,6
# 5,8,6,3
# 5,8,6,3,4
# 5,8,6,3,4,8
# 8
# 8,6
# 8,6,3
# 8,6,3,4
# 8,6,3,4,8
# 6
# 6,3
# 6,3,4
# 6,3,4,8
# 3
# 3,4
# 3,4,8
# 4
# 4,8
# 8

# nested loop

# for y in range(1, 11):
#     for x in range(1,11):
#         print(y,"*", x,"=",y*x)

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

for i in range(0, 4):
    for j in range(0, 5):
        print(i, end=" ")
    print()

# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4

# for i in range(0, 4):
#     for j in range(0, 5):
#         print(j, end=" ")
#     print()

# 0 1 2 3 4
# 5 6 7 8 9
# 10 11 12 13 14
# 15 16 17 18 19

# k = 0
# for i in range(0, 4):
#     for j in range(k, k+5):
#         print(j, end = " ")
#     k = j+1
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(0,5):
#     for j in range(0, i):
#         print("*", end=" ")
#     print()

#

# * * * * *
# * * * *
# * * *
# * *
# *
#
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*",end=" ")
#     print()

#          *
#       *  *
#    *  *  *
#  * *  *  *


#
# for i in range(0,4):
#     for j in range(4, i, -1):
#         print(" ", end=" ")
#     for k in range(0, i+1):
#         print("*", end=" ")
#     print()

 #     *
 #   * * *
 #  * * * * *
 #* * * * *  * *

# for i in range(0, 5):
#     for j in range(5, i+1, -1):
#         print(" ", end=" ")
#     for k in range(0, i+1):
#         print("*", end=" ")
#     for l in range(0, i):
#         print("*", end=" ")
#     print()
# 65 = A
# A
# A B
# A B C
# A B C D
# A B C D E

# 65
# 65 66
# 65 66 67
# 65 66 67 68
# 65 66 67 68 69


# for i in range(0,5):
#     for j in range(0,i+1):
#         print(chr(65+j),end=" ")
#     print()
# n = 5
# for( i in range(0, n))
# o(n) o
#
# rder of n
#
# arr = [4,7, 6, 3, 1,8,9]
# arr = [10, 30, 40, 60, 80, 100] n log n

# arr = [8, 9, 3, 6, 1, 4]
# n = len(arr)
# print(arr)
# for i in range(0, n-1):
#     for j in range(0, n-1-i):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# x = [4,1,28,9,5,11]
#
# n = len(x)
#
# for i in range(0,n-1):
#     for j in range(0,n-1-i):
#         if x[j]>x[j+1]:
#             x[j],x[j+1] = x[j+1],x[j]
# print(x)

x = [2,3,4,5,6,1,1,3,2]
# n = len(x)
# for i in range(n-1,-1,-1):
#     print(x[i],end= " ")

# list = []
# for i in x:
#     if i not in list:
#         list.append(i)
# print(list)

# n = len(x)
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if x[i] == x[j]:
#             print(x[i], end=",")

# Reverse an Array
# /
# arr = [-2,1,-3,4,-5,8,-10,7,-6,5]

# def reverse_array(arr):
#
#     temp_array = []
#     temp_array2 = []
#     c = 0
#
#     for i in range(0,len(arr)):
#         if arr[i]>=0:
#
#             temp_array.append(arr[i])
#
#         else:
#             temp_array2.append(arr[i])
#
#     for i in (temp_array2 + temp_array):
#
#         arr[c] = i
#         c+=1
#
# reverse_array(arr)
# print(arr)

# arr = [1,2,3,4,5,6]
#
# def reverse_array(arr):
#     n = len(arr)
#     temp = [0]*n
#
#     for i in range(0,n):
#         temp[i] = arr[n-i-1]
#
#     for i in range(0,n):
#         arr[i] = temp[i]
#
# reverse_array(arr)
# print(arr)


# arr = [2,3,4,5,6,8,9,10]
#
# def max_and_min(arr):
#     n = len(arr)
#     max = arr[0]
#     min = arr[0]
#     for i in range(0,n):
#         if arr[i]>max:
#             max = arr[i]
#         if arr[i]<min:
#             min = arr[i]
#
# sum = max+min
#
# max_and_min(arr)
# print(sum)


