"""
You get three variables, an amount of boxes N, the maximum amount of boxes
you can carry M, and how parts you can divide it up by P.
The algorithm should do the following: Split the boxes into equal piles with
the smallest difference amount and continuously split the piles if they are
greater than what you can carry. Return how many piles you have at the end

Example:

Input: 11, 2, 2.
11 = 6 + 5
6 = 3 + 3
5 = 3 + 2
3 = 2 + 1 (3 times)
Output: 7

Output should be 7. Four piles of 2 and three pile of 1.
"""

def count_piles(boxes_count, max_carry_size, parts):
   final_count = [0]
   def reduce_piles(boxes_count, max_carry_size, parts):
     max_parts = min(boxes_count, parts)
     smallest_pile = int(boxes_count / parts) or 1
     piles = [smallest_pile for x in range(0, max_parts)]
     leftovers = boxes_count - sum(piles)
     for index in range(0, leftovers):
       piles[index] += 1
     for pile in piles:
         if pile <= max_carry_size:
           final_count[0] += 1
         else:
           reduce_piles(pile, max_carry_size, parts)
   reduce_piles(boxes_count, max_carry_size, parts)
   return final_count[0]

assert count_piles(11, 2, 2) == 7
assert count_piles(3, 2, 5) == 3
assert count_piles(100, 1, 3) == 100
