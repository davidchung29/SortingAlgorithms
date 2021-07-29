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

def shell_sort(li):
  gap = len(li)//2
  while gap>0:
    a = 0
    b = gap
    while b<len(li):
      if li[a] > li[b]:
        temp = li[a]
        li[a], li[b] = li[b], temp
      a+=1
      b+=1
      c = a
      while c-gap > -1:
        if li[c-gap] > li[c]:
          li[c-gap],li[c] = li[c],li[c-gap]
        c-=1
    gap //= 2
  print(li)

  
def bogosort(li):
  while (is_sorted(li)== False):
      n = len(li)
      for x in range (0,n):
          r = random.randint(0,n-1)
          li[x], li[r] = li[r], li[x]
  print(li)
    
def mergesort_david(li): #O(NlogN) -> O(N)Space#
  if len(li) > 1:
    q = len(li)//2
    a = li[q:]
    b = li[:q]
    mergesort_david(a)
    mergesort_david(b)

    x=y=z=0
    while x<len(a) and y<len(b):
      if a[x] < b[y]:
        li[z] = a[x]
        x+=1
      else:
        li[z] = b[y]
        y+=1
      z+=1
    while x < len(a):
      li[z] = a[x]
      x+=1
      z+=1
    while y < len(b):
      li[z] = b[y]
      y+=1
      z+=1
def insert_heap(li,element):
  a = element
  li.append(a)
  i = li.index(a)
  while i>1 and (li[i] < li[i//2]):
    li[i], li[i//2] = li[i//2], li[i]
  return li

def leaf_count(a,b):
  x = a - (2**b)
  if x > 0:
    return leaf_count(x, b+1)
  elif x<=0:
    return a


def delete_min(li):
  li[1] = li[len(li)-1]
  li = li[:-1]
  a = 1
  b = 2 if li[2] < li[3] else 3
  leaves = leaf_count(len(li),0)
  y = -1*leaves

  while (li[b] < li[a]) and (a<(len(li)-leaves+1)):
    li[a], li[b] = li[b], li[a]
    a = b
    if b < len(li)-2:
      b = b+1 if li[b+1] < li[b+2] else b+2
    else:
      break

  return li

def heap_sort(li):
  temp = []
  for i in li:
    insert_heap(temp, i)
  return temp
