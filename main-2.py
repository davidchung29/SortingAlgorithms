def selectionSort(li):
  for p in range(len(li)):
    for j in range(p,len(li)):
      if li[j]<li[p]:
        temp = li[p]
        li[p] = li[j]
        li[j] = temp
  return li

