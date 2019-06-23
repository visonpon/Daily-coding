'''
题目描述：
输入是一排树，每棵树上结的有果子，这个数字代表果子的种类（注意，不是数目）。
让你从某个位置开始向右连续的去摘果子，只有两个篮子，每个篮子只能放同一类果子。
如果向右遍历的过程中没有果子可以摘了，或者果篮里没法放当前树的果子，那么就停止，问总的能摘多少果子。
'''
#soulution:求一个数组的最长连续子数组，要求这个子数组中最多只存在两个不同的元素。
'''
双指针，计算双指针区间内的所有元素的个数，这个个数就是我们要求的能摘取的果子个数。同时在移动的过程中要保证，双指针区间内的元素种类最多为2.
'''

class solution(object):
  def fruit(self,tree):
    left,right=0,0
    res=0
    cnt= collections.defaultdict(int)
    while right<len(tree):
      cnt[tree[right]] +=1
      while len(tree)>2:
        cnt[tree[left]] -=1
        if cnt[tree[left]]==0:
          del cnt[tree[left]]
        left +=1
      res = max(res,right-left+1)
      right +=1
  return res
  
        
          
    
    
    
