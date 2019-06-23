'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target，找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别，如果数组中不存在目标值，返回 [-1, -1]。
'''

#二分查找&双指针
class solution(object):
  def search(self,a,target):
    if len(a)==0:
      return [-1,-1]
    elif target < a[0] or target > a[-1]:
      return [-1,-1]
    elif:
      l=0
      r=len(a)-1
      while l<r:
        mid = (l+r)//2
        if target > a[mid]:
          l = mid+1
        elif target < a[mid]:
          j = mid -1
       elif target == a[mid]:
        l=r=mid
        while l-1>=0 and a[l-1]==target:
          l -=1
        while r+1<= len(a)-1 and a[r+1]==target:
          r +=1
        return [l,r]
    return [-1,-1]
          
          
        
