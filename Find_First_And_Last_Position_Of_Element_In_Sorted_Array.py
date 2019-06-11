class solution(object):
  def search(self,a,target):
    l=0
    r=len(a)-1
    while l<r:
      mid = (l+r)//2
      if target == a[mid]:
        tem=mid
        while tem>0 and a[mid-1]==target:
          tem -=1
        while mid<len(a)-1 and a[mid+1]==target:
          mid +=1
        return [tem,mid]
      elif target > a[mid]:
        l=mid+1
      else:
        r = mid-1
    return[-1,-1]
        
