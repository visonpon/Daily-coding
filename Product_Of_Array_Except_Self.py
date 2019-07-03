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
      
      
class solution2(object):
  def product(self,arr):
    output = [1]
    for i in range(len(arr)-1):
      output.append(ouput[-1]*arr[i])
      
    right = 1
    for j in range(len(arr)-1,-1,-1):
      output[i] = right*output[i]
      right *=num[i]
    
    return output
      
