'''
Find a triplet subsequence in an array
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
      
