'''
@Time : 2022/1/9 23:38 

@Author : zhouyanlong

@File : easy.py 

@Software: PyCharm

@Description:

'''
#print("a".join(list(map(lambda x:x,"123"))))
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
# -*- coding:utf-8 -*-
"""给定一个int整数数组A及其大小n，请编写一个函数，找出索引m和n，只要将m和n之间的元素排好序，整个数组就是有序的。注意：n-m应该越小越好，即找出符合条件的最短序列。请返回一个二元组，元组的两个元素分别代表所求序列的起点和终点。(原序列位置从0开始标号,若原序列有序，返回[0,0])。要求A中元素均为正整数。
测试样例：
[1,4,6,5,9,10],6
返回：[2,3]"""
# class Rearrange:
#     def findSegment(self, A, n):
#         # write code here
#         B=A[:]
#         c=[]
#         B.sort()
#         for i in range(n):
#             if B[i]!=A[i]:
#                 c.append(i)
#         if c == []:
#             return [0,0]
#         else:
#             return [c[0], c[-1]]
# Rearrange().findSegment([1,2,10,1,8,9],6)
# -*- coding:utf-8 -*-
"""给定一个int n，返回n的阶乘的末尾连续的零的个数"""
# class Factor:
#     def getFactorSuffixZero(self, n):
#         # write code here
#         def f(n):
#             if n == 1:
#                 return 1
#             else:
#                 return n * f(n - 1)
#
#         cheng = f(n)
#         c = []
#         su = str(cheng)[::-1]
#         print(su)
#         for i in range(len(su)):
#             if su[i] == "0":
#                 c.append(0)
#             else:
#                 break
#         print(len(c))
#         return len(c)
# Factor().getFactorSuffixZero(6)
# -*- coding:utf-8 -*-
"""现有一堆球颜色是红色(R)、黄色(Y)、绿色(G)或蓝色(B)各若干个，现在随机选四个球分别放入四个槽中，得到一个序列。例如，RGGB(槽1为红色，槽2、3为绿色，槽4为蓝色)，需要你猜出这个颜色序列的组合。比如，你可能猜YRGB。要是猜对了某个槽的颜色，则算一次“猜中”。要是只是猜对了颜色但槽位猜错了，则算为一次“伪猜中”。要注意，“猜中”不能算入“伪猜中”。给定两个string A和guess。分别表示颜色序列的组合和一个猜测。需要返回一个int数组，数组第一个元素为猜中的次数，第二个元素为伪猜中的次数"""
# class Result:
#     def calcResult(self, A, guess):
#         # write code here
#         t = ['R', 'Y', 'G', 'B']
#         persudo = 0
#         for i in t:
#             print(i)
#             persudo += min(A.count(i), guess.count(i))
#             print(persudo)
#         #print(persudo)
#         sum = 0
#         for i in range(len(A)):
#             if A[i] == guess[i]:
#                 sum += 1
#                 persudo -= 1
#         return sum, persudo
# Result().calcResult("RGBY","GGRR")
# -*- coding:utf-8 -*-
"""
井字棋
给定一个二维数组board，代表棋盘，其中元素为1的代表是当前玩家的棋子，0表示没有棋子，-1代表是对方玩家的棋子。当一方棋子在横竖斜方向上有连成排的及获胜（及井字棋规则），返回当前玩家是否胜出
[
[1, 0, 1], 
[1, -1,-1], 
[1, -1, 0]
]
"""
# class Board:
#     def checkWon(self, board):
#         # write code here
#         c=d=e=f=0
#         for i in range(len(board)):
#             if board[0][i]==1:
#                 c+=1
#             if board[i][0]==1:
#                 d+=1
#             if board[i][len(board)-1]==1:
#                 e+=1
#             if board[i][i]==1:
#                 f+=1
#         if c==len(board) or d==len(board) or e==len(board)or f==len(board):
#             return 1
#         else:
#             return 0
# print(Board().checkWon([[1, 0, 1,0], [1, -1, -1,1], [1, -1, 0,0],[-1,-1,-1,-1]]))
"""
使用位运算交换字符
使用亦或^
"""
# a=[1,2]
# a[0]^=a[1]
# a[1]^=a[0]
# a[0]^=a[1]
"""已知一个数组A及它的大小n，在读入这串数的时候算出每个数的秩，即在当前数组中小于等于它的数的个数(不包括它自身)。从而返回一个int数组，元素为每次加入的数的秩
[1,2,3,4,5,6,7],7
返回：[0,1,2,3,4,5,6]"""
# class Rank:
#     def getRankOfNumber(self, A, n):
#         # write code here
#         c=[]
#         d=[]
#         for i in range(n):
#             d.append(A[i])
#             d.sort()
#             c.append(d.index(A[i]))
#         return c
"""二分法查找（数字必须有序）时间复杂度logn"""
#lst=[20,50,22,-22,0,15,222,28,29,99,1999,100823,55,35,5,1,2,3,8,9,55,10239,234234]
# def erfen(x,lst=lst):
#     a=sorted(lst)
#     i=0
#     j=len(a)
#     while i<=j:
#         mid=int((i+j)/2)
#         if x==a[mid]:
#             return mid
#         elif x<a[mid]:
#             j=mid+1
#         else:
#             i=mid-1
#     return False
# print(erfen(10239))
"""已知正整数n，将其分为0到多个25、10、5、1这四个数的和。如n为11可分为一个10和一个1，或者分为两个5和一个1"""
# class Coins:
#     def countWays(self, n):
#         coins = [1, 5, 10, 25]
#         dp = [0 for i in range(n + 1)]
#         dp[0] = 1
#         #dp=[1, 0, 0, 0, 0, 0, 0]
#         #i=0,j=1,2,3,4,5,6
#         #i=1,j=5,6
#         #i=2,j=
#         #i=3,j=
#         #coin的长度
#         for i in range(4):
#             #coin到总价钱的长度
#             for j in range(coins[i], n + 1):
#                 dp[j] += dp[j - coins[i]]
#         print(dp)
#         return dp[n]
# print(Coins().countWays(6))
"""itertools.permutations 求字符串的全排序
输入“abc”
输出['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""
# from itertools import permutations
# a="abc"
# lst=list(permutations(a,len(a)))
# b=[]
# for i in lst:
#     s = ""
#     for j in i:
#         s+=j
#     b.append(s)
# print(b)
"""给定一个N阶方阵int[][]mat及其阶数n，若方阵中某个元素为0，则将其所在的行与列清零。返回改变后的int[][]方阵"""
#[[1,2,3],[0,1,2],[0,0,1]]
# class Clearer:
#     def clearZero(self, mat, n):
#         #出现0的行号 set去重
#         row=set()
#         #出现0的列号 set去重
#         col=set()
#         #im为二位列表的下标和值
#         for i,k in enumerate(mat):
#             #jn为二维列表中的列表的下标和值
#             for j,l in enumerate(k):
#                 if l==0:
#                     row.add(i)
#                     col.add(j)
#         print(row,col)
#         for i in row:
#             for j in range(n):
#                 mat[i][j]=0
#         for i in col:
#             for j in range(n):
#                 mat[j][i]=0
#         print(mat)
#         return mat
# Clearer().clearZero([[1,2,3],[0,1,2],[0,0,1]],3)
"""请按连续重复字母压缩的方式将该字符串压缩，返回结果为string，比如，字符串“aabbcccccaaa”经压缩会变成“a2b2c5a3”，若压缩后的字符串没有变短，则返回原先的字符串。注意保证串内字符均由大小写英文字母组成"""
# class Zipper:
#     def zipString(self, iniString):
#         zipStr = ""
#         strCnt = 1
#         for i in range(len(iniString) - 1):
#             #如果字符相同，变量加一
#             if iniString[i + 1] == iniString[i]:
#                 strCnt += 1
#             #否则，等于字符加变量，在重置变量
#             else:
#                 zipStr += iniString[i] + str(strCnt)
#                 strCnt = 1
#         print(zipStr)
#         #把最后不满足的字符加上
#         zipStr += iniString[-1] + str(strCnt)
#         return zipStr if len(zipStr) < len(iniString) else iniString
# Zipper().zipString("aabbc")
"""给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列
给出的数组为 [20, 70, 110, 150] , 目标值为90
返回一个数组 [1,2] ，numbers[0]+munbers[1]=20+70=90"""
# class Solution:
#     def twoSum(self , numbers , target ):
#         # write code here
#         for i in range(len(numbers)-1,0,-1) :
#             sub = target - numbers[i]
#             if sub in numbers and numbers.index(sub) != i :
#                 List =[numbers.index(sub)+1,i+1]
#                 return List
"""给定一个字符串，找出最长的不具有重复字符的子串的长度。例如，“abcabcbb”不具有重复字符的最长子串是“abc”，长度为3。对于“bbbbb”，最长的不具有重复字符的子串是“b”，长度为1
输入abcabcbb
输出abc
输入bbb
输出b"""
# class Solution:
#     def lengthOfLongestSubstring(self , s ):
#         if s=="":
#             return int(0)
#         else:
#             a = []
#             b = []
#             for i in range(len(s)):
#                 for j in range(len(s) - i):
#                     a.append(s[j:len(s) - i])
#             print(a)
#             for m in range(len(a)):
#                 for n in range(len(a[m])):
#                     # print(a[m][n])
#                     if a[m].count(a[m][n]) != 1:
#                         c = 0
#                         break
#                     else:
#                         c = 1
#                 if c == 1:
#                     b.append(a[m])
#             f = []
#             for l in b:
#                 f.append(len(l))
#             return max(f)
# print(Solution().lengthOfLongestSubstring("aabcd"))
#
#
# @param height int整型一维数组
# @return int整型
#
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#

