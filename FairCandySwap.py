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
