#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_value = prices[1] - prices[0]
  max_range = len(prices)
  for i in range(max_range - 1):
    for j in range(i+1, max_range):
      diff = prices[j] - prices[i]
      if diff > max_value:
        max_value = diff
  return max_value


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))