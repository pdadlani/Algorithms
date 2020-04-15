#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_batches = float('inf')
  for item in recipe:
    if item not in ingredients.keys():
      return 0

    num_batches = ingredients[item] // recipe[item]

    if num_batches < min_batches:
      min_batches = num_batches

  return min_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))