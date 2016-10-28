#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
from telnetlib import ECHO
import cmd

def copyspecial_doc():
  print \
"""Copy Special exercise
Google's Python class

usage: [--todir dir][--tozip zipfile] dir [dir ...]

Write a utility that takes the arguments:
--todir {dirpath} 
--tozip {filepath}
[ {filepath}, ... ]

default: Looks for files with the pattern '__{text}__' in the name
and prints them out.

--todir copies the files to the {dirpath} 
and makes the directory if needed.

--tozip zips the files into the {filepath}
---------------------------------------------------
"""

#
def get_source_filenames( dir_list ):
  """ get the filenames in a directory and extract the ones
 that contain the pattern __{text}__"""
  
  # loop over all directories given
  abs_file_list = [] 
  for dirname in dir_list :
    # get the abs path of the directory
    try:
      full_path = os.path.abspath( dirname )
    except:
      print '*Directory error:', dirname
      sys.exit(1)
      
    # get a list of filenames in the directory
    try:
      file_list = os.listdir( full_path )
    except:
      print '*File list error:', full_path
      sys.exit(1)

    #print 'full_path:', full_path, '\nfile_list:', file_list
    # for each special file add to the list
    for filename in file_list :
      match = re.search('__\w+__', filename)
      if match :
        abs_file_list.append(os.path.join(full_path, filename))
        
  #for filename in abs_file_list :
  #  print filename
  return abs_file_list

#
def copy_todir( dirname, abs_file_list):
  """ copy the files to the directory and create
the directory if it does not exist """
  
  try:
    full_path = os.path.abspath( dirname )
  except:
    print '*Directory error:', dirname
    sys.exit(1)
  try:
    if not os.path.exists(full_path) :
      #print 'making directory:', full_path
      os.makedirs(full_path)
  except:
      print "*Cannot make directory: ", full_path
      sys.exit(1)
      
  try:
    for filename in abs_file_list :
      #print "copy from ", filename, ' to ', full_path
      shutil.copy(filename, full_path)
  except:
      print "*File copy error: from ", filename, ' to ', full_path
      sys.exit(1)    
  return

#
def copy_tozip( filename, abs_file_list):
  """ zip the files in the file list to the specified file """

  cmd = 'zip -j ' + filename + ' '
  cmd += ' '.join(abs_file_list)
  #print 'zip cmd:', cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status :
    print '*Zip error: ', status, output
    sys.exit(1) 
  return
    
# debug for IDE
def IDE_TestArgs( arg0 ):
  print 'IDE_TestArgs()'
  #test = 'dirtest'
  #test = 'ziptest'
  test = 'default'
  # start with the name of the program
  testargs = [arg0]
  # pick which test parameters to set
  if test == 'dirtest' : testargs.append('--todir'); testargs.append(' output')
  if test == 'ziptest' : testargs.append('--tozip'); testargs.append(' output.zip')
  # all tests use the local directory
  testargs.append('.')
  print 'TestArgs( ', testargs, ')'
  return testargs
#
#
#
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # get a list of the command line arguments
  args = sys.argv
  
  # if this is being run from and IDE then fake the command line for ease of testing
  if __name__ != "__main__":
    args = IDE_TestArgs(sys.argv[0])
    
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = args[1:]

    
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  #print 'copyspecial args:', todir, tozip, args
  # Call your functions
  copyspecial_doc()
  abs_file_list = get_source_filenames( args )
  if '' != todir : 
    copy_todir( str(todir), abs_file_list )
  else: 
    if '' != tozip : 
      copy_tozip( str(tozip), abs_file_list )
    else: 
      print '\n'.join( abs_file_list )
  
  
if __name__ == "__main__":
  main()
