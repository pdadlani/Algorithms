#!/usr/bin/python

import sys

def making_change(amount, denominations, cache=None):
  if cache is None:
    cache = [0] * (amount+1)
    cache[0] = 1

  for coin in denominations:
    for higher_amts in range(coin, amount+1):
      difference = higher_amts - coin
      cache[higher_amts] += cache[difference]
  return cache[amount]
    


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")