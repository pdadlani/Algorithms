#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  options = ['rock', 'paper', 'scissors']
  output = []

  if n == 0:
    return [[]]
  elif n == 1: 
    return [[options[0]]] + [[options[1]]] + [[options[2]]]
  else:
    r1 = rock_paper_scissors(n-1)
    for spot in r1:
      output.append(spot + [options[0]])
      output.append(spot + [options[1]])
      output.append(spot + [options[2]])
  return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')