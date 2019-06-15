'''
input:[1,3,5,4,7]

output:2---[1,3,5,7] & [1,,3,4,7]

https://blog.csdn.net/qq_37108878/article/details/85705088
'''
class Solution(object):
  def findLIS(self,num):
    len = nums.size()
    lenght = np.ones(len)
    cnt = np.ones(len)
    max_len = 1
    res = 0
    for i in range(len):
      for j in range(i):
        if (nums[i] > nums[j]):
          if (length[i] == length[j] + 1):
            cnt[i] += cnt[j]
          else if (length[i] < length[j] + 1) :
            length[i] = length[j] + 1
            cnt[i] = cnt[j]
      max_len = max(max_len, length[i])
      
    for i in range(len):
      if (length[i] == max_len)
        res += cnt[i]
    return res
