'''
Find a triplet subsequence in an array
solution:线性扫描数组，如果小于等于first,赋值给first，如果小于等于second，赋值给second，如果没地方赋值了，说明递增序列中的第三个找到了
'''
class solution(obejct):
  def triplet(self,arr):
    if len(num)<3 or num is None:
      return False
    res=[float('inf'),float('inf')]
    for a in arr:
      if a <= res[0]:
        res[0]=a
      elif a<=res[1] and a>res[0]:
        res[1]=a
      else:
        return True
    return Fasle
      
