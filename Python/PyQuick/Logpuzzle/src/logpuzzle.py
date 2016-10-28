#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
#
# https://developers.google.com/edu/python/exercises/log-puzzle

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
#
#
#
def key_place( item ) :
  retValue = item[-10:]   # default last 10 items
  match = re.search(r'-(\w+).jpg$', item )
  if match :
    retValue = match.group(1) # last word before .jpg
  #print 'key: ', retValue
  return retValue

 #
 #
 #
def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  
  #print filename
  file_handle = open(filename, 'rU')
  text = file_handle.read()
  file_handle.close()

  sorting = 'animal'
  # get the hostname from the filename
  # filename: something_code.google.com
  # hostname: http://code.google.com
  match = re.search(r'(\w+)_(.+)', filename)
  hostname = 'http://code.google.com'   # default hostname
  if match :
    hostname = 'http://' + match.group(2)
    sorting = match.group(1)            # animal or place filename
  #print 'hostname: ', hostname, 'sorting: ', sorting
  
  # extract the puzzle url's from the log
  table_list = re.findall(r'GET\s(\S+/puzzle/\S+)\s', text)
  #print '\n'.join(table_list)
  
  # add url's to a dictionary to remove duplicates
  dict_list = {}
  for item in table_list:
    url = hostname + item   # add the hostname to the url
    dict_list[url] = 0      # the value isn't important, just the key
    
  # sort the url's to arrange the image slices
  if sorting == 'animal' :
    retValue = sorted(dict_list.keys()) # the sorted url's in the keys is the answer
  else:
    retValue = sorted(dict_list.keys(), key=key_place) # the sorted url's in the keys is the answer
      
  #print '\n'.join(retValue)
  return retValue
  
#
#
#
def key_fname( filename ):
  retVal = 0
  match = re.search('(\d+)$', filename)
  if match :
    retVal = int(match.group(1))
  #print 'filename: ', filename, ' key: ', retVal
  return retVal
#
#
#
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  #print dest_dir, img_urls
  try:
    full_path = os.path.abspath( dest_dir )
  except:
    print '*Directory error:', dirname
    sys.exit(1)
  #print 'full_path: ', full_path
  try:
    if not os.path.exists(full_path) :
      #print 'making directory:', full_path
      os.makedirs(full_path)
  except:
    print "*Cannot make directory: ", full_path
    sys.exit(1)
    
  count = 0
  filename = 'img'
  for url in img_urls :
    basename = 'img' + str(count)
    filename = full_path + '/' + basename
    count += 1
    #print 'copy from :', url, '\nto: ', filename
    print '.',
    try:
      urllib.urlretrieve(url, filename)
      #shutil.copy(filename, full_path)
    except:
      print "\n*File download error: from ", url, '\n to ', filename
      #sys.exit(1)

  # write an html file with the images referred from the url's
  # do this instead of making references to local file images because
  # the VM has some issue with Python urllib open and it takes
  # several minutes per operation to perform or it just fails 100% of the time
  header = """<verbatim>
<html>
<body>
"""
  footer = """
</body>
</html>
""" 
  file_handle_web = open('index_web.html', 'w')
  file_handle_web.write( header )

  for url in img_urls:
    file_handle_web.write( '<img src=' + url + '>')

  file_handle_web.write( footer )
  file_handle_web.close()

  #
  # continued development on an non VM and urllib is workable
  #
  # write html file to reference images in directory
  file_list = sorted(os.listdir( full_path ), key=key_fname)
  #print file_list
  file_handle_file = open('index_file.html', 'w')
  file_handle_file.write( header )

  for file in file_list:
    file_handle_file.write( '<img src=' + full_path + '/' + file + '>')

  file_handle_file.write( footer )
  file_handle_file.close()
  
#
#
#
def main():
  args = sys.argv[1:]

  #print args
  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
