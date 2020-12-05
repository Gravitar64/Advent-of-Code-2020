import numpy as np
import time
import math


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [zeile.strip() for zeile in f]


def löse(puzzle, dx, dy):
  px = py = 0
  maxX, maxY = len(puzzle[0]), len(puzzle)
  counter = 0
  while True:
    px, py = px+dx, py+dy
    if py >= maxY:
      return counter
    if puzzle[py][px % maxX] == '#':
      counter += 1


def BrotherLui(dx, dy):  # Brother Lui aka Thomas
  bottom = len(puzzle)
  width = len(puzzle[0])
  x = y = 0
  encountered = ''
  while y < bottom:
    encountered += puzzle[y][x]
    x = (x + dx) % width
    y += dy
  return encountered.count('#')

def MasterBe(puzzle):
  index = 0
  counter = 0
  for slope in puzzle[1:]:
    index += 3
    if index >= len(slope):
      index -= len(slope)
    if slope[index] == "#":
      counter += 1
  return counter

puzzle = puzzle_einlesen('Tag_03.txt')

start = time.perf_counter()
print('GR',löse(puzzle, 3, 1), time.perf_counter()-start)

start = time.perf_counter()
print('MB',MasterBe(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print('BL',BrotherLui(3, 1), time.perf_counter()-start)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

start = time.perf_counter()
lösung = 1
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  lösung *= löse(puzzle, dx, dy)
print('GR',lösung, time.perf_counter()-start)

start = time.perf_counter()
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print('BL',np.prod([BrotherLui(*slope) for slope in slopes]),time.perf_counter()-start)


