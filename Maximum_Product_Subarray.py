'''
题目描述：给一个数组，找出其中连续的子数组中，相乘最大的一组
'''

class solution(obejct):
  def max(self,arr):
    if len(arr) == 0:
      return 0
    min_tem = arr[0]
    max_tem = arr[0]
    result = arr[0]
    for i in range(1,len(arr)+1):
      a = arr[i]*min_tem
      b = arr[i]*max_tem
      c = arr[i]
      max_tem = max(max(a,b),c)
      min_tem = min(min(a,b),c)
      result = max_tem if max_tem >result else result
    return result
