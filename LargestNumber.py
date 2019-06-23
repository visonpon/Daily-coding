'''
题目描述：给定一个包含非负数的列表，重新排列，使其最终组合之后的整数最大。例如：给定列表[3, 30, 34, 5, 9], 返回的最大整数是9534330
相当于对列表中的数字进行排序。使用冒泡排序、快排等都可以。
重要的是怎么决定两个整数的先后顺序，如3，30和34：正确的顺序是34330，正确的判断思路是根据组合后的数字哪个大进行排序。
'''

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
          
