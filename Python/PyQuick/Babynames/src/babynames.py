#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# https://developers.google.com/edu/python/exercises/baby-names

import sys
import re
import platform
import os

def babynames_doc():
  print \

"""Google's Python Class
Baby Names exercise

  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
"""
  
"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def print_list( print_list, filename, flag):
  """ print the list to a file or to the console """
  
  text = '\n'.join(print_list)
  try:
    if flag :
      fhandle = open( filename, 'w')  # out to a file
      fhandle.write( text )
      fhandle.close()
    else:
      print text                      # out to the console
  except:
    print '* File write error: ', filename
 
# read the names and ranks from a preformatted .html file   
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  try:
    file_handle = open(filename, 'rU')
    text = file_handle.read()
    file_handle.close()
  except:
    print '* File not found: ', filename
    sys.exit(1)
  
  # find the year of the table
  match = re.search("Popularity in (\d+)", text)
  if not match :
    print '*Can\'t find year in data. File:', filename
    sys.exit(1)    
  year = match.group(1)
  
  # find the ranking and the names in the table
  table_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  
  # add names and rank to a dictionary to remove duplicates
  # list is [(rank, boy, girl), . . .]
  dict_rank = {}
  for item in table_list:
    (rank, boy, girl) = item
    if boy not in dict_rank :    # only keep the first instance
      dict_rank[boy] = rank
    if girl not in dict_rank :
      dict_rank[girl] = rank
      
  # now format the dictionary entries as "name rank"
  retVal = []
  list_tuples = dict_rank.items()
  # list format [(name, rank), . . .]
  for item in list_tuples :
    retVal.append(item[0] + ' ' + item[1])
    
  # sort the formatted list alphabetically
  retVal = sorted(retVal)
  # insert the year into the front of the list
  retVal.insert(0, year)
  
  return retVal

# test routine for IDE
def main_test():
  
  file_list = ["baby1990.html",\
"baby1992.html",\
"baby1994.html",\
"baby1996.html",\
"baby1998.html",\
"baby2000.html",\
"baby2002.html",\
"baby2004.html",\
"baby2006.html",\
"baby2008.html"]
  #print file_list
  for filename in file_list:
    list_rank = extract_names(filename)
    print_list( list_rank, filename + '.summary', False)

#
# Running on Windows the file wildcards *.* are not expanded
# by the command.com shell. Add filename expansion for * in
# filenames.
#
def expand_filenames( path ) :
  """ expand *.* wildcards in Windows filenames into a file list()"""
  
  #print 'expand_filenames(', path, ')'
  # get the full path to the file
  dirpath = os.path.dirname(path)
  if '' == dirpath :
    dirpath = '.\\'             # this is the local directory
  abspath = os.path.abspath(dirpath)
  
  # add a slash if there isn't one on the end
  match = re.search(r'\\$', abspath)
  if not match :
    abspath += '\\'
  #print 'path:', dirpath, 'abspath:', abspath

  # get the filename from the path
  basename = os.path.basename(path)
  #print 'basename:', basename

  # escape any RE wildcard characters in the filename
  text = re.escape(basename)
  #print 'text:', text

  # find any '\*' in the filename
  match = re.search(r'\\\*', text )
  if  not match :
    # none found so just return the full file path
    retVal = [ abspath + path ]   
    return retVal

  # convert the '\*' to '.*' for RE
  text = re.sub(r'\\\*', r'.*', text );
  text +='$'              # match text right justified to filename
  #print 'text:', text

  # get a list of the files in the directory
  filelist = os.listdir( dirpath )
  #print filelist

  # loop over the files to match the filename pattern
  retVal = []
  for filename in filelist :
    #print 'filename:', filename
    match = re.search( text, filename ) # match filename to directory filename
    if match :
      retVal.append( abspath + filename ) # add matching filename to the list
      
  #print retVal
  return retVal

def main(*m_args):
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  # Overrides argv when testing (interactive or below)
  #print m_args
  if m_args:
    sys.argv = ["babynames.py"] + list(m_args)
        
  args = sys.argv[1:]
  #print args

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # process for Windows OS
  if platform.system() == 'Windows' :
    for filename in args :
      filename_list = expand_filenames( filename )
      # For each filename, get the names, then either print the text output
      # or write it to a summary file 
      for item in filename_list :
        list_rank = extract_names(item)
        print_list( list_rank, item + '.summary', summary)
  else:
    # process for Linux OS
    # For each filename, get the names, then either print the text output
    # or write it to a summary file    
    for filename in args:
      list_rank = extract_names(filename)
      print_list( list_rank, filename + '.summary', summary)
    
if __name__ == '__main__':
  main()
  
