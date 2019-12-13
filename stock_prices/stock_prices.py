#!/usr/bin/python

import argparse

def find_max_profit(prices):
  best_profit = None
  for i in range(0, len(prices)):
    for j in range(0, len(prices)):
      if j > i:
        if best_profit == None:
          best_profit = prices[j]-prices[i]
        if (prices[j]-prices[i]) > best_profit:
          best_profit = prices[j]-prices[i]
  return best_profit

print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))