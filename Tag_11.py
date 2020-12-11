import time
import pygame as pg
from pygame._sdl2.video import Window


def puzzle_einlesen(datei):
  with open(datei) as f:
    return {(x,y):0 for y,zeile in enumerate(f) for x,char in enumerate(zeile) if char == 'L'}

def zeichne_map(map):
  screen.fill((0,0,0))
  for (s,z),val in map.items():
    x,y = s*tile_size, z*tile_size
    if val == 0:
      pg.draw.rect(screen,(0,200,0),(x,y,tile_size,tile_size))
    else:
      pg.draw.rect(screen,(200,0,0),(x,y,tile_size,tile_size))
  pg.display.flip()      


def occ_neighbors(map,x,y,see):
  count = 0
  for dx, dy in ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)):
    for m in range(1,see+1):
      x2,y2 = x+dx*m, y+dy*m
      if (x2,y2) in map and map[(x2,y2)] == 0: break
      if map.get((x2,y2),0) == 1:
        count += 1
        break
  return count    

def löse(map,see,toleranz):
  occ1 = 0
  while True:
    zeichne_map(map)
    map2 = map.copy()
    for pos in map:
      n = occ_neighbors(map,*pos,see)
      if n == 0:
        map2[pos] =1
      elif n >= toleranz:
        map2[pos] =0
    occ2 = sum(map2.values())
    if occ1 == occ2: return occ2
    occ1 = occ2
    map = map2
    


pg.init()
screen = pg.display.set_mode((1000,1000))
w = Window.from_display_module()
w.position = 1920,150
tile_size = 10


puzzle = puzzle_einlesen('Tag_11.txt')


start = time.perf_counter()
print(löse(puzzle,1,4), time.perf_counter()-start)

start = time.perf_counter()
print(löse(puzzle,100,5), time.perf_counter()-start)
