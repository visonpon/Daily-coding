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
