class compare(str):
  def __init__(x,y):
    return x+y > y+x
    
class solution:
  def largestnumber(self,num):
    largest = sorted([str(v) for v in num],key=compare)
    largest=''.join(largest)
    
    return 0 if largest[0]=='0' else largest

  #solution2
  class solution(object):
    def smaller(self,a,b):
      if str(a)+str(b) < str(b)+str(a):
        return True
      else:
        return Fasle
    
    def largetnumber(self,num):
      resultstr=''
      for i in range(len(num)):
        for j in range(i+1,len(num)):
          if self.smaller(num[i],num(j)):
            tmp = num[i]
            num[i] = num[j]
            num[j] = num[i]
      for i in range(len(num)):
        resultstr= resultsrt + str(i)
        
     if resultstr[0]=='0':
      return '0'
     return resultstr
          
