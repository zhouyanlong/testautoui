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
"""求子串"""
# a="abcd"
# b=[]
# for i in range(len(a)):
#     for j in range(len(a)-i):
#         b.append(a[j:len(a)-i])
# print(b)
"""
根据这个来写循环
i=0 j=0123
i=1 j=123
i=2 j=23
i=3 j=3
取其中一个来取切片的值，如i=0 j=0,1,2,3 当i=0,j=0时，字母为a，我想要的是a j=1时ab,j=2时abc,j=3时abcd，即a[i,j+1]
"""
# a="abcd"
# b=[]
# for i in range(len(a)):
#     #for j in range(len(a) - i):
#     for j in range(i,len(a)):
#         b.append(a[i:j+1])
# print(b)
# -*- coding:utf-8 -*-

# class Parenthesis:
#     def chkParenthesis(self, A, n):
#         a = list(A)
#         stack =[]
#         for i in a:
#             if i == '(':
#                 stack.append(i)
#             elif i == ')':
#                 if not stack:
#                     return False
#                 else:
#                     stack.pop()
#             else:
#                 return False
#         return True

"""排序"""
# def paixu():
#     d, b, c, = input().split()
#     a = []
#     a.append(d)
#     a.append(b)
#     a.append(c)
#     print(max(a))
"""排序的优化方案"""
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

"""两种方式，list中的数据分别为int和str类型"""
# a = list(map(int, input().split(" ")))
# print(a,type(a))

# a = input().split(" ")
# print(a,type(a))
"""判断输入list是否有序"""
# a=input()
# b=list(map(int,input().split(" ")))
# c=b[:]
# c.sort()
# print("sorted"if c==b or c==b[::-1] else "unsorted" )
"""最大公约数+最小公倍数"""
# a,b=list(map(int, input().split(" ")))
# def yue(a=a,b=b):
#     c = 0
#     if a>=b:
#         for i in range(1,b+1):
#             if a%i==0 and b%i==0:
#                 c=i
#         return c
#     elif a<b:
#         for i in range(1,a+1):
#             if a%i==0 and b%i==0:
#                 c=i
#         return c
# def bei(a=a,b=b):
#     c=0
#     if a>=b:
#         for i in range(a,a*b+1):
#             if i%a==0 and i%b==0:
#                 return i
#     else:
#         for i in range(b,a*b+1):
#             if i%a==0 and i%b==0:
#                 return i
"""优化方案"""
# n, m = map(int,input().split())
# ma = max(n, m)
# mi = min(n, m)
# r = ma % mi
# while r != 0:
#     ma = mi
#     mi = r
#     r = ma % mi
# print(int(mi + n*m//mi))
"""输入一个数字，奇数位变1，偶数位变0"""
# a=list(map(int,input()))
# print(a,type(a))
# for i in range(len(a)):
#     if a[i]%2==0:
#         a[i]=0
#     else:
#         a[i]=1
# print(a)

"""方案1：取list中的数字拼成一个数字"""
# sum=0
# for i in range(len(a)):
#     ss=a[i]*10**(len(a)-i-1)
#     sum+=ss
# print(sum)
"""方案2，先转化成str，再强转成int"""
# str1=""
# for i in a:
#     str1+=str(i)
# print(int(str1))
"""求质数"""
# def f(a):
#     for i in range(2,a):
#         if a%i==0:
#             return "YES"
#         else:
#             return "NO"
# count=0
# for i in range(100,1000):
#     if f(i)=="NO":
#         count+=1
# print(count)

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
"""假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
1.你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
2.如果不能获取到任何利润，请返回0"""
# class Solution:
#     def maxProfit(self , prices) -> int:
#         b=[]
#         if len(prices)!=1:
#             for i in range(len(prices)-1):
#                 now=prices[0]
#                 prices.pop(0)
#                 # if i<len(prices)-1:
#                 earn = max(prices) - now
#                 b.append(earn)
#             if max(b)>=0:
#                 return max(b)
#             else:
#                 return int("0")
#         else:
#             return int("0")
# print(Solution().maxProfit([1]))
"""求最长回文串"""
# b=[]
# a="abcba"
# for i in range(len(a)):
#     for j in range(len(a) - i):
#         b.append(a[j:len(a) - i])
# c=[]
# for m in b:
#     if m==m[::-1]:
#         c.append(m)
# d=[]
# for i in range(len(c)):
#     d.append(len(c[i]))
# print(max(d))
"""有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度
输入：[[1,2,3],[4,5,6],[7,8,9]],3 
返回值：[[7,4,1],[8,5,2],[9,6,3]]"""
# class Solution:
#     def rotateMatrix(self , mat,n):
#         # write code here
#         a = []
#         b = []
#         for j in range(n):
#             for i in range(n):
#                 a.append(mat[n - i - 1][j])
#         for i in range(0, len(a), n):
#             b.append(a[i:i + n])
#         print(b)
#         return b
# Solution().rotateMatrix([[1,2,3,4],[4,5,6,4],[7,8,9,4],[1,2,3,4]],4)
"""超级简便方法
1:解包裹得到list中的list，2使用[::-1]转置，在使用zip拼接"""
# class Solution:
#     def rotateMatrix(self , mat,n):
#         return zip(*mat[::-1])
"""给定两个长度为n字符串A和B，如果能将A从中间某个位置分割为左右两部分字符串（不能为空串），并将左边的字符串移动到右边字符串后面组成新的字符串可以变为字符串B时返回true。
例如：如果A=‘youzan’，B=‘zanyou’，A按‘you’‘zan’切割换位后得到‘zanyou’和B相同，返回true"""
# class Solution:
#     def solve(self , A , B ):
#         a=0
#         if A==B:
#             #print("aa")
#             return "false"
#         else:
#             for i in range(len(A)):
#                 str1=A[i:]+A[:i]
#                 if str1 == B:
#                     a=1
#             return a==1
# print(Solution().solve("abcd","abcd"))
