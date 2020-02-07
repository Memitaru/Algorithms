#!/usr/bin/python

'''
Loop over arguements
Track the current lowest price and the current max profit
If the value is lower than the lowest price, lowest price equals that value
Else if value minus current lowest price is higher than current max profit, set that to max profit
Return max profit after looping over all values
'''

import argparse

def find_max_profit(prices):

  curr_min = None
  max_profit = None

  for price in prices:
    if curr_min is not None and max_profit is None:
      max_profit = price - curr_min
    if curr_min is None:
      curr_min = price
    if (curr_min is not None) and (max_profit is not None) and  (price - curr_min) > max_profit:
      max_profit = price - curr_min
    if (curr_min is not None) and price < curr_min:
      curr_min = price
  
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))