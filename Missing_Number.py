'''
题目描述：给出从 0 - n的数，找出其中缺少的那个。
'''

class solution(obejct):
  def missingnum(self,num):
    all_num = sum(range(1,len(num)+1))
    for i in num:
      all_num -=i
    return all_num
