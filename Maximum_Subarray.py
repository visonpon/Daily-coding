'''
题目描述：给定一个整型数组，找到其中连续的数组，使其和最大
需要维护两个变量，分别为局部最优curr_sum，和全局最优max_sum。

遍历数组时，从第一个元素开始累加，并赋值给局部最优curr_sum，当局部最优为负数时，可放弃对应子串，重置局部最优为0。
每一次计算出新的局部最优时，与当前全局最优比较，将较大的值付给全局最优。
最后通过一次遍历，找到子串的最大。

原文：https://blog.csdn.net/zjrn1027/article/details/80348510 

'''

class solution(object):
  def maxsub(self,arr):
    cur_sum=0
    max_sum =0
    for n in arr:
      if cur_sum < 0:
        cur_sum = 0
      cur_sum +=n
      max_sum = max(cur_sum,max_sum)
    return max_sum
