class solution(object):
  def merge(self,intervels):
    if not intervels:
      return []
    intervels.sort(key:lambda x : x.start)
    res = [intervels[0]]
    for i in range(1,len(intervels)):
      if intervels[i].start <= res[-1].end
        res[-1].end = max(intervels[i].end,res[-1].end)
      else:
        res.append(intervels[i])
      return res
    
    '''
    insert intervels
    '''
    class soultion(object):
      def insert(self,intervels,newintervels):
        intervels.append(newintervels)
        intervels.sort(key:lambda x:x.start)
        s = len(intervels)
        
        res =[]
        for i in range(s):
          if res ==[]:
            res.append(intervels[i])
          else:
            if res[-1].start < intervels[i].start <= res[-1].end :
              res[-1].end = max(intervels[i].end, res[-1].end)
            else:
              res.append(res[i])
        return res
       
            
