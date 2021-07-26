def selectionSort(li):
  for p in range(len(li)):
    for j in range(p,len(li)):
      if li[j]<li[p]:
        temp = li[p]
        li[p] = li[j]
        li[j] = temp
  return li

def insertion_sort(li):
  for x in range(len(li)):
    key = li[x]
      
    y = x-1
    while y>=0 and key < li[y]:
      li[y+1] = li[y]
      y-=1
    li[y+1] = key
  print(li)

