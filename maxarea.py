'''
leetcode11---container with most water
solution--- use two pointers ,one start at the start place,the other at the end.
'''

class solution(object):
  def maxarea(self,height):
    ans = 0
    l = 0
    r = len(height)-1
    while l<r:
      ans = max[ans,min(height[l],height[r])*(r-1)]
      if height[l]<height[r]:
        l +=1
      else:
        r -=1
    return ans
      
