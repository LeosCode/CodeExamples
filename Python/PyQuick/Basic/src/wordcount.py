#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys

def wordcount_doc():
  print \
"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
""" 

"""
Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
# ##

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

dictWords = {}

def add_to_dict( line ):
  """ add the words in a line of text to the dictionary and count them. """
  
  #print 'add_to_dict(', line[:-1], ')'
  # break line into list of words at white space
  listWords = line.split()    
  for word in listWords:
    word = word.lower()       # remove differences from case
    if word in dictWords :
      dictWords[word] += 1
    else:
      dictWords[word] = 1
  
  
def read_file( filename ):
  """ read a file a line at a time and add the words to the dictionary."""
  
  try:
    fp = open( filename, 'rU')  #open file for reading
    for line in fp :            # get one line at a time
      #print line,
      add_to_dict( line )       # add words to dictionary
    fp.close()
    return False
  except:
    print '* File not found ', filename
    return True

def print_dictionary( nMax ):
  """print the dictionary of words in sorted order along with the word count."""
  
  # sort the dictionary of words
  listWords = dictWords.items()   # make a list of the dictionary entries
  listWords = sorted(listWords)   # sort the list by the keys (words)

  # limit the output for debug purposes
  if nMax > 0 :
    listWords = listWords[0:nMax]

  # print the list of words and counts
  for word in listWords:          # get each entry in the list
    print word[0], '\t\t' , word[1] # format and print it
    
  
def print_words(filename):
  """ print the words in wordcount order from the file """
  
  #print 'print_words(', filename, ')'
  
  # read the file and fill in a dictionary with the words
  if read_file( filename ) :
    return  # did not open file
  
  # sort the dictionary of words
  listWords = dictWords.items()   # make a list of the dictionary entries
  listWords = sorted(listWords)   # sort the list by the keys (words)

  # print the list of words and counts
  for word in listWords:          # get each entry in the list
    print word[0], '\t\t' , word[1] # format and print it
    
def key_fn( tupleItem ):
  """ return the second item in the tuple """
  return tupleItem[1]

def print_top(filename):
  """ print the top 20 wordcount words from the file """
  #print 'print_top', filename, ')'
  
    # read the file and fill in a dictionary with the words
  if read_file( filename ) :
    return  # did not open file
  
  # sort the dictionary of words
  listWords = dictWords.items()   # make a list of the dictionary entries
  listWords = sorted(listWords, key=key_fn, reverse=True)   # sort the list by the keys (words)
  #print listWords

  # print the list of words and counts
  for word in listWords[0:19]:      # get first 20 entries in the list
    print word[0], '\t\t' , word[1] # format and print it

def main_test():
  """ test wordcount under IDE shell. """
  #print 'main_test()'
  wordcount_doc()
  print '\n--count small.txt\n'
  print_words('small.txt')
  print '\n--topcount alice.txt\n'
  print_top('alice.txt')
    
def main():
  
  #print sys.argv
  # IDE shell breaks the options flag as a separate argument
  nArgs = 3
  if sys.argv[1] == '--':   # -- passed as it's own argument
    nArgs = 4
    
  if len(sys.argv) != nArgs:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[nArgs - 2]
  filename = sys.argv[nArgs - 1]
  
  if nArgs == 3 :
    print option[2:]
    option = option[2:]

    
  if option == 'count':
    print_words(filename)
  elif option == 'topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main_test() # test in IDE environment
  
# otherwise run main() as interactive utility
