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
  return li

def bubble_sort(li):
  for i in range(len(li)):
    for j in range(0, len(li)-i-1):
      if li[j]>li[j+1]:
        li[j],li[j+1] = li[j+1],li[j]
  return li

def shell_sort_david(li):
  gap = len(li)//2
  while gap>0:
    a = 0
    b = gap
    
