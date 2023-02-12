import numpy

def mergesort(items):
  return _mergesort(0, len(items), items, list(items))

def _mergesort(start, end, items, output):
  
  if len(items) <= 1:
    return items
  
  left = 0
  right = len(items)
  mid = int(len(items)/2)

  left_half = _mergesort(start, start + mid, items[left:mid], output[left:mid])
  right_half = _mergesort(start + mid - 1, start + right, items[mid:right], output[mid:right])
  
  
  
  left_item = None
  right_item = None
  
  if len(left_half) > 0:
    left_iter = iter(left_half)
    left_item = next(left_iter)

  if len(right_half) > 0:
    right_iter = iter(right_half)
    right_item = next(right_iter)

  pos = 0
  
  while (left_item != None or right_item != None):
    
    if left_item != None and right_item != None:
      if left_item >= right_item:
        output[pos] = right_item
        
        pos = pos + 1
        
        
        try:
          right_item = next(right_iter)
          
        except StopIteration:
          right_item = None
       

        
      elif right_item >= left_item:
        output[pos] = left_item
        
        pos = pos + 1
        
        try:
          left_item = next(left_iter)
        except StopIteration:
          left_item = None
        
        
    elif right_item == None:
      output[pos] = left_item
      
      pos = pos + 1
      try:
        left_item = next(left_iter)
      except StopIteration:
        left_item = None
      
    elif left_item == None:
      output[pos] = right_item
      
      pos = pos + 1
      try:
        right_item = next(right_iter)
      except StopIteration:
        right_item = None
      
    
    
  
  return output

import math
from concurrent.futures import ThreadPoolExecutor
class Context:
  def __init__(self, items):
    self.pool = ThreadPoolExecutor(len(items) - 1)
  

def mergesort_concurrent(items):
  context = Context(items)
  return _mergesort_concurrent(context, 0, len(items), items, list(items))

def _mergesort_concurrent(context, start, end, items, output):
  
  if len(items) <= 1:
    return items
 
  left = 0
  right = len(items)
  mid = int(len(items)/2)

  left_future = context.pool.submit(_mergesort_concurrent, context, start, start + mid, items[left:mid], output[left:mid])
  right_future = context.pool.submit(_mergesort_concurrent, context, start + mid - 1, start + right, items[mid:right], output[mid:right])
  left_half = left_future.result()
  right_half = right_future.result()
  
  
  
  left_item = None
  right_item = None
  
  if len(left_half) > 0:
    left_iter = iter(left_half)
    left_item = next(left_iter)

  if len(right_half) > 0:
    right_iter = iter(right_half)
    right_item = next(right_iter)

  pos = 0
  
  while (left_item != None or right_item != None):
    
    if left_item != None and right_item != None:
      if left_item >= right_item:
        output[pos] = right_item
        
        pos = pos + 1
        
        
        try:
          right_item = next(right_iter)
          
        except StopIteration:
          right_item = None
       

        
      elif right_item >= left_item:
        output[pos] = left_item
        
        pos = pos + 1
        
        try:
          left_item = next(left_iter)
        except StopIteration:
          left_item = None
        
        
    elif right_item == None:
      output[pos] = left_item
      
      pos = pos + 1
      try:
        left_item = next(left_iter)
      except StopIteration:
        left_item = None
      
    elif left_item == None:
      output[pos] = right_item
      
      pos = pos + 1
      try:
        right_item = next(right_iter)
      except StopIteration:
        right_item = None

  return output

print(mergesort([8, 7, 5, 4, 2, 1, 6, 10, -1]))
print(mergesort_concurrent([101, -4, -3, 8, 50, 7, 5, 4, 2, 1, 6, 10, -1, 60]))   
  

  