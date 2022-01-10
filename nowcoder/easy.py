'''
@Time : 2022/1/9 23:38 

@Author : zhouyanlong

@File : easy.py 

@Software: PyCharm

@Description: 
'''

"""#最大公约数"""
#1：时间和空间复杂度高
# class Solution:
#     def gcd(self, a: int, b: int) -> int:
#         if a <= b:
#             if b % a == 0:
#                 return a
#             else:
#                 for i in range(1, int(a + 1 / 2)):
#                     if b % i == 0 and a % i == 0:
#                         c=i
#                 return c
#         else:
#             if a % b == 0:
#                 return b
#             for i in range(1, int(b + 1 / 2)):
#                 if b % i == 0 and a % i == 0:
#                     c=i
#             return c
#2使用递归
# class Solution:
#     def gcd(self, a, b):
#         if b == 0:
#             return a
#         else:
#             return self.gcd(b, a % b)

"""排序"""
# def paixu():
#     d, b, c, = input().split()
#     a = []
#     a.append(d)
#     a.append(b)
#     a.append(c)
#     print(max(a))
"""优化方案"""
# ln = list(map(int, input().split()))
# print(max(ln))
"""冒泡"""
# def paixu():
#     d, b, c, = input().split()
#     a = []
#     a.append(d)
#     a.append(b)
#     a.append(c)
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print(a)
"""打印正方形"""
# a=input()
# for i in range(int(a)):
#     for j in range(int(a)):
#         if j==int(a)-1:
#             print("*")
#         else:
#             print("*",end=" ")
"""直角三角形图案"""
#i控制行数，j控制每行的个数
# a=int(input())
# for i in range(a):
#     for j in range(i + 1):
#         if j == i:
#             print("*")
#         else:
#             print("*", end=" ")
"""棱形图案"""
# a=int(input())
# for i in range(2*a+1):
#     if i<=a:
#         print((a-i)*" "+(i+1)*"* ")
#     else:
#         print(" "*(i-a)+"* "*(2*a+1-i))
"""空心三角形图案"""
# a=int(input())
# for i in range(a):
#     if i >= 2 and i != a - 1:
#         print("* " + (i - 1) * "  " + "* ")
#     else:
#         print((i + 1) * "* ")