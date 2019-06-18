class solution(object):
  def quick_sort(start,end,arr):
    if star < end:
      l,r = start ,end
      base = arr[l]
      while l < r:
        while l < r and arr[r] > base:
          r -=1
        arr[l] = arr[r]
        while l < r and arr[l] < =base:
          l +=1
        arr[r] = arr[l]

      arr[l]=base
    
      quick_sort(start,i-1,arr)
      quick_sort(j+1,end,start)
    return arr
      
      
        
        
    
