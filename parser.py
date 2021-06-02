# -*- coding: utf-8 -*-
import re, collections, sys, os

ALL=set()

def tokens(text):
    """
    Get all words from the corpus
    """
    t = re.sub("[A-Z]", lambda x: "_" + x.group(0).lower(), text)
    return set(re.findall('[a-z]+', t))

def print_words(fn):
  global ALL
  with open(fn, 'r') as f:
      WORDS = tokens(f.read())
      ALL = set.union(ALL, WORDS)

top_dir = sys.argv[1]
if os.path.isfile(top_dir):
  print_words(top_dir)
else:
  g = os.walk(top_dir)
  for path,dir_list,file_list in g:
    for file_name in file_list:
      f = os.path.join(path, file_name)
      print_words(f)

for v in ALL:
  print v
