#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import random
import sys

def mimic_doc():
  print \
"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.

Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.
-------------------------------------------------------
"""

"""
Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.
"""

# show part of dictionary for debug
def print_dict( dictItem ):
  end = 20
  count = 0;
  for keyItem in dictItem:
    print keyItem, dictItem[keyItem]
    count += 1
    if count > end : break

#
def mimic_dict(filename):
  #print """\nmimic_dict(filename) Returns mimic dict mapping each word to list of words which follow it."""
  dictLists = {'':['']}
  # read in the file as a text string
  try:
    fHandle = open(filename, 'rU')
    text = fHandle.read()
    fHandle.close()
  except:
    print '* File not found:', filename
    return dictLists
  #split the text into list of words
  wordList = text.split()
  dictLists[''] = [wordList[0]]   # first entry is first word in file
  #print wordList
  count = 1;                      # need to track where we are in the list
  end = len(wordList)
  for word in wordList:
    if count >= end :             # no 'next' word in the list
      break
    
    if word in dictLists:
      #print '+'
      dictLists[word].append(wordList[count])   # append to 'next' word list for this word
    else:
      #print'.'
      dictLists[word] = [wordList[count]]       # add this word list to the dictionary
    count += 1
    
  #print_dict( dictLists )
  return dictLists


def print_mimic(mimic_dict, word):
  #print """\nprint_mimic(mimic_dict, word) Given mimic dict and start word, prints 200 random words."""
  #print mimic_dict
  charCount = 0                 # track line length
  lineLimit = random.randint( 25, 60 )  # pick a line length
  for count in range(200):      # limit the run to 200 words
    print word,                 # print this word
    charCount += len(word)      # track line length so far
    if charCount > lineLimit : 
      print                     # start a new line after limit chars
      charCount = 0
      lineLimit = random.randint( 25, 60 )
      
    # pick a random 'next' word from the entries for this word
    if word not in mimic_dict :
      word = ''                 # use '' if word is not in dictionary
    word = random.choice(mimic_dict[word])  


# test function for IDE
def main_test():
  
  mimic_doc()
  
  dictMimic = mimic_dict('alice.txt')
  print_mimic(dictMimic, '') 
  
  
# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dictMimic = mimic_dict(sys.argv[1])
  print_mimic(dictMimic, '')


if __name__ == '__main__':
  main_test() # test in IDE environment
  
# otherwise run main() as interactive utility
