#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

def verbing_doc():
  print """
 D. verbing
 Given a string, if its length is at least 3,
 add 'ing' to its end.
 Unless it already ends in 'ing', in which case
 add 'ly' instead.
 If the string length is less than 3, leave it unchanged.
 Return the resulting string.
 """
 
def verbing(s):
  print 'verbing(', s, ')\t',
  if len(s) < 3 :
    return s
  ##print 'last 3:', s[-3:]
  if s[-3:] == 'ing' :
    retVal = s + 'ly'
  else:
    retVal = s + 'ing'
  return retVal

def not_bad_doc():
  print """
 E. not_bad
 Given a string, find the first appearance of the
 substring 'not' and 'bad'. If the 'bad' follows
 the 'not', replace the whole 'not'...'bad' substring
 with 'good'.
 Return the resulting string.
 So 'This dinner is not that bad!' yields:
 This dinner is good!
 """
 
def not_bad(s):
  print 'not_bad(', s, ')\t',
  notindex = s.find('not')
  badindex = s.find('bad')
  retVal = s
  if notindex != -1 and badindex != -1 :
    if notindex < badindex :
      retVal = s[:notindex-1]
      retVal += ' good'
      retVal += s[badindex + 3:]
  # +++your code here+++
  return retVal

def front_back_doc():
  print """
 F. front_back
 Consider dividing a string into two halves.
 If the length is even, the front and back halves are the same length.
 If the length is odd, we'll say that the extra char goes in the front half.
 e.g. 'abcde', the front half is 'abc', the back half 'de'.
 Given 2 strings, a and b, return a string of the form
  a-front + b-front + a-back + b-back
  """


def front_back(a, b):
  print 'front_back(', a, b, ')\t',
  aLen = len(a)
  aHalf = aLen - (aLen / 2)
  bLen = len(b)
  bHalf = bLen - (bLen / 2)
  retVal =  a[0:aHalf]
  retVal += b[0:bHalf]
  retVal += a[-(aLen/2):]
  retVal += b[-(bLen/2):]
  ##print a, b, retVal
  return retVal


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'Google Course PyQuick\nPython Test Exercises ', 'String2'
  
  #print 'verbing'
  verbing_doc()
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  #print 'not_bad'
  not_bad_doc()
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  #print 'front_back'
  print front_back_doc()
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
