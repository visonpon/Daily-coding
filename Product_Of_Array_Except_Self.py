'''
题目描述：给定整数数组，返回一个新数组，使得新数组的索引i中的每个元素都是原始数组中除i中的所有数字的乘积
'''

class soultion(obejct):
  def product(self, arr):
  sum = 1
  list = []
    for i in range(len(arr)):
      for j in arr:
        sum *= j
      sum = sum // arr[i]
      list.append(sum)
      
      
