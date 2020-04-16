#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache={}):
  options = ['rock', 'paper', 'scissors']
  output = []

  if n == 0: return [[]]
  elif n == 1:
    return [[x] for x in options]
  elif n not in cache:

    prev_output = rock_paper_scissors(n-1)
    for item in prev_output:
      output.append(item + [options[0]])
      output.append(item + [options[1]])
      output.append(item + [options[2]])
      cache[n] = output
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')