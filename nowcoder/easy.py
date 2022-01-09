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
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

