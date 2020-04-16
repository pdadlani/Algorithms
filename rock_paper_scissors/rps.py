#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  output = []

  if n == 0: return [[]]
  elif n == 1:
    return [[x] for x in options]
  else:
    prev_output = rock_paper_scissors(n-1)
    # return [[['rock'] + x for x in prev_output] + [['paper'] + x for x in prev_output] + [['scissors'] + x for x in prev_output]]
    # output = []
    for item in prev_output:
      output.append(item + ['rock'])
      output.append(item + ['paper'])
      output.append(item + ['scissors'])
    #   output += [option] + rock_paper_scissors(n-1)
    return output

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')