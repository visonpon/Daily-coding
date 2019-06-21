class compare(str):
  def __init__(x,y):
    return x+y > y+x
    
class solution:
  def largestnumber(self,num):
    largest = sorted([str(v) for v in num],key=compare)
    largest=''.join(largest)
    
    return 0 if largest[0]=='0' else largest
