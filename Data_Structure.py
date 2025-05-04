
# class Node:
#     def __init(self,data):
#         self.data = data
#         self.next = None
#
# class single_link_list:
#     def __init__(self):
#         self.head = None
#
#     def display(self):
#         if self.head is None:
#             print("linked list is Empty:")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,"-->",end = " ")
#             temp = temp.next
#
# l = single_link_list()
# n = Node(10)
# l.head = n
# n1 = Node(20)
# l.head.next = n1
# l.display()


























# Double lineked List

# class Node:
#     def __init(self,data):
#         self.data = data
#         self.next = None
#
# class Double_linked_List:
#     def __init(self):
#         self.head = None
#
#     def display(self):
#         if self.head is None:
#             print("linked List is Empty:")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,"-->",end = " ")
#             temp = temp.next
#
# L = Double_linked_List()
# n = Node(10)
# L.head = n
# n1 = Node(20)
# n1.prev = n
# n2 = Node(30)
# n2.prev =n1
# n3 = Node(40)
# n3.prev = n2
# L.display()















# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Single_linked_list:
#     def __init__(self):
#         self.head = None
#
#     def insert_begining(self,data):
#         nb = Node(data)
#         nb.next = self.head
#         self.head = nb
#
#     def insert_end(self,data):
#         ne = Node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = ne
#
#     def display(self):
#         if self.head is None:
#             print("Linked List is Empty:")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,"-->",end = " ")
#                 temp = temp.next
#
# l = Single_linked_list()
# n = Node(10)
# l.head = n
# n1 = Node(20)
# l.head.next = n1
# n2 = Node(30)
# l.head.next = n1
# l.insert_begining(5)
# l.insert_end(30)
# l.display()





























## Single Linked List

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Single_liked_list:
#     def __init__(self):
#         self.head = None
#     def display(self):
#         if self.head is None:
#             print("Linked list is Empty")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,"-- >",end = " ")
#                 temp = temp.next
#
#
# l = Single_liked_list()
# n = Node(10)
# l.head = n
# n1 = Node(20)
# l.head.next = n1
# n2 = Node(30)
# n1.next = n2
# n3 = Node(40)
# n2.next = n3
# l.display()












## Single Linked List

# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class single_linked_List:
#     def __init__(self):
#             self.head = None
#     def display(self):
#         if self.head is None:
#             print("Linked List is Empty")
#
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,"-->",end=" ")
#                 temp = temp.next
#
# l = single_linked_List()
# n = node(10)
# l.head(n)
# n1 = node(20)
# l.head.next = n1
# l.display()
















## Binary Searching Algorithm

# list = []
# n = int(input("Enter The Element to be Inserted"))
# print("Enter the ",n,"values")
# for i in range(n):
#     list.append(int(input()))
# list.sort()
# s = int(input("Enter the Searched Element "))
# low = 0
# high = len(list)-1
# mid = 0
# while low<=high:
#     mid = (low+high)//2
#     if list[mid]==s:
#         print(s,"Is found the Element",mid+1)
#         break
#     elif list[mid]>s:
#         high = mid-1
#     else:
#         low = mid+1
# else:
#     print(s,"None of the Element")
#
#
#
#
#
#
#
#
#
#
#
#
# ##  Linear seraching Algorithm
#
# list = []
# n = int(input("Enter The Element to be Inserted"))
# print("Enter",n,"values")
# for i in range(n):
#     list.append(int(input()))
# s = int(input("Enter the Element to be searched :"))
# if s in list:
#     print(s,"is found at position",list.index(s))
# else:
#     print(s,"is not Found in the List")


# stack = []
# while(True):
#     print("1-Operation,2-Pop_operation,3-Display_operation")
#     choice = int(input("Enter Your Choice"))
#     match choice:
#         case 1:
#             n = int(input("Enter Your Element:"))
#             stack.append(n)
#         case 2:
#             for i in stack:
#                 print(i)
#         case 3:
#             stack.pop(0)
#
#         case default:
#             exit(0)













# stack = []
# while(True):
#     print("1-Push, 2- Display, 3- pop")
#     choice = int(input("Enter your choice: "))
#     match choice:
#         case 1:
#             n = int(input("Enter a number: "))
#             stack.append(n)
#         case 2:
#             for i in stack:
#                 print(i)
#
#         case 3:
#             stack.pop(0)

        # case default:
        #     exit(0)






# def push():
#     n = int(input("Enter the Element: "))
#     if len(stack) == 0:
#         stack.append(n)
#         print("Data append - ")
#     else:
#         stack.insert(0,n)
#         print(n,"Inserted into the Stack")
#
# def pop():
#     if len(stack) == 0:
#         print("The Stack is Empty")
#     else:
#         print(stack[0],"is deleted from stack")
#         del stack[0]
# def display():
#     if len(stack) == 0:
#         print("Stack is empty")
#     else:
#         print("Element of stack")
#
#         for ele in stack:
#             print(ele)
#         print("Top of the Stack",stack[0])


