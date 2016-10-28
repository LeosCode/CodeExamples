#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

import sys

def remove_adjacent_doc():
  print """
 D. Given a list of numbers, return a list where
 all adjacent == elements have been reduced to a single element,
 so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
 modify the passed in list.
 """

def remove_adjacent(nums):
  print 'remove_adjacent(', nums , ')'
  #print 'len(nums):', len(nums)

  if len(nums) < 3 :
    return nums
  
  retValue = [nums[0]]
  prevItem = retValue[0]
  for item in nums:
    #print 'prevItem:', prevItem, 'item: ', item
    if prevItem != item :
      retValue.append( item )
    prevItem = item
    
  #print retValue
  return retValue

def linear_merge_doc():
  print """
 E. Given two lists sorted in increasing order, create and return a merged
 list of all the elements in sorted order. You may modify the passed in lists.
 Ideally, the solution should work in "linear" time, making a single
 pass of both lists.
  """
  
def linear_merge(list1, list2):
  print 'linear_merge(', list1, ' ', list2, ')'

  # get the length of the lists
  # find which list is shorter
  # shorter = shorter longer = longer
  # loop over items in shorter
  # merged.append(shorter) merged.append(longer)
  # merge.append(longer)

  # determine which is the shorter list of items
  len_list1 = len(list1)
  len_list2 = len(list2)
  if len_list1 < len_list2 :
    shorter = list1
    shorter_len = len_list1
    longer = list2
    longer_len = len_list2
  else:
    shorter = list2
    shorter_len = len_list2
    longer = list1
    longer_len = len_list1

  #print 'shorter:', shorter
  #print 'longer:', longer

  # loop over the shorter list of items and merge
  # them with the longer list of items
  retVal = []
  for count in range(shorter_len) :
    item1 = shorter[count]     # get the items
    item2 = longer[count]
    if item1 <= item2 :
      retVal.append(item1)     # smaller item goes first
      retVal.append(item2)
    else:
      retVal.append(item2)      # smaller item goes first
      retVal.append(item1)

  # loop over the remaining longer list of items
  # and add them to the merged list
  for count in range(count+1, longer_len) :
    retVal.append(longer[count])
  
  #print retVal
  return retVal


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'Google Course PyQuick\nPython Test Exercises ', 'List2'
  #print 'remove_adjacent'
  remove_adjacent_doc()
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  #print 'linear_merge'
  linear_merge_doc()
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
