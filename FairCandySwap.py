'''
题目描述：
Alis和Bob有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。

他们想交换一个糖果棒，使得都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

要求返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个，保证答案存在。
'''

#solution1:遍历数组求和，然后求两者的差值，再遍历两个人的糖果，看是否有符合该差值的
class solution(object):
  def faircandyswap(self,a,b):
    sum_a = 0
    sum_b = 0
    ans=[]
    for i in range(len(a)-1):
      sum_a += a[i]
    for j in range(len(b)-1):
      sum_b += b[j]
    
    temp = sum_a-sum_b
    for i in range(len(a)-1):
      for j in range(len(b)-1):
        if (a[i]-b[j])*2==tmep:
          ans[0] = a[i]
          ans[1] = b[j]
          break;
    return ans
    
#########:
####################################
'''solution two'''
class solution2(object):
  def faircandyswap(self,a,b):
    dif = sum(a) - sum(b)
    a,b = set(a),set(b)
    for i in a:
      if i+dif//2 in b:
        return [i,i+dif//2]
    return[]
