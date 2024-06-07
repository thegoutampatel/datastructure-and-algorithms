# Time Complexity:
# 1. Best or average case scenario : O(n logn)
# 2. Worst case scenario: O(n^2)

## Method definition of partition
def partition(arr, p, q):
  pivot = arr[p]
  i = p
  for j in range(i+1, q+1):
    if arr[j] <= pivot:
      i += 1
      ## swap between the values of arr[i] and arr[j]
      arr[i], arr[j] = arr[j], arr[i]
  ## final swap between the value of arr[i] and arr[p]
  arr[i], arr[p] = arr[p], arr[i]
  return i

## Method definition of quickSort
def quickSort(arr, p, q):
  if p < q:
    ## Divide and Conquer Approach
    ## 1. Divide
    ## function calling for the partition method
    mid = partition(arr, p, q)
    ## recursive function call for the left subtree
    quickSort(arr, p, mid-1)
    ## recursive function call for the right subtree
    quickSort(arr, mid+1, q)
  return arr

## Driver code
arr = [50, 70, 29, 67, 12, 15, 46, 100, 26, 29]
p = 0
q = len(arr) - 1
## function calling
result = quickSort(arr, p, q)
print(result)

#Random Quick Sort

import random

## Method definition of randomizedPartition
def randomizedPartition(arr, p, q):
  ## random pivot index
  randomPivotIndex = random.randrange(p,q)
  ## swap the random index with the first index 
  arr[p], arr[randomPivotIndex] = arr[randomPivotIndex], arr[p]
  return partition(arr, p, q)

## Method definition of partition
def partition(arr, p, q):
  pivot = arr[p]
  i = p
  for j in range(i+1, q+1):
    if arr[j] <= pivot:
      i += 1
      ## swap between the values of arr[i] and arr[j]
      arr[i], arr[j] = arr[j], arr[i]
  ## final swap between the value of arr[i] and arr[p]
  arr[i], arr[p] = arr[p], arr[i]
  return i

## Method definition of quickSort
def quickSort(arr, p, q):
  if p < q:
    ## Divide and Conquer Approach
    ## 1. Divide
    ## function calling for the partition method
    mid = randomizedPartition(arr, p, q)
    ## recursive function call for the left subtree
    quickSort(arr, p, mid-1)
    ## recursive function call for the right subtree
    quickSort(arr, mid+1, q)
  return arr

## Driver code
arr = [50, 70, 29, 67, 12, 15, 46, 100, 26, 29]
p = 0
q = len(arr) - 1
## function calling
result = quickSort(arr, p, q)
print(result)