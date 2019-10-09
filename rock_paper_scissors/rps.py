#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n <= 0: # empty array b/c you can't have less than 1
    return [[]]
  
  moves = [["rock"], ["paper"], ["scissors"]]
  if n == 1:
    return moves

  final_value = []
  choices = rock_paper_scissors(n - 1)
  for item in moves:
    for value in choices:
      final_value.append(item + value)
  return final_value

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')