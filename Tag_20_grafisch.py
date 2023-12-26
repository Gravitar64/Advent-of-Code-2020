import time, math, regex 
import pygame as pg


def read_puzzle(file):
  with open(file) as f:
    return [[element for element in zeile.split('\n')] for zeile in f.read().split('\n\n')]


def rot_flip(id, tile):
  for i in range(4):
    yield (id, i), tile
    yield (id, i+4), tile[::-1]  # vertikal gespiegelt
    tile = list(map(''.join, zip(*tile[::-1])))  # rotiert um 90 Grad im UZS


def create_map(sol, tilesV, GRDS):
  karte = ['']*GRDS*8
  for pos, idv in enumerate(sol):
    puzzle_zeile = pos // GRDS
    for zeile in range(8):
      karte[puzzle_zeile*8+zeile] += tilesV[idv][zeile+1][1:9]
  return karte

def create_map2(sol, tilesV, GRDS):
  karte = ['']*GRDS*10
  for pos, idv in enumerate(sol):
    puzzle_zeile = pos // GRDS
    for zeile in range(10):
      karte[puzzle_zeile*10+zeile] += tilesV[idv][zeile]
  return karte  



def solve(puzzle):
  anzTiles = len(puzzle)
  GRIDSIZE = int(math.sqrt(anzTiles))
  tilesV = {idv: variante for tile in puzzle for idv,
            variante in rot_flip(int(tile[0][5:-1]), tile[1:])}

  def match_tiles(pos, idv, idvs):
    spalte, zeile = pos % GRIDSIZE, pos // GRIDSIZE
    prüfO = zeile == 0 or tilesV[idv][0] == tilesV[idvs[pos-GRIDSIZE]][-1]
    prüfL = spalte == 0 or [z[0] for z in tilesV[idv]] == [
        z[-1] for z in tilesV[idvs[pos-1]]]
    return prüfO and prüfL

  def dfs(pos, idvs, ids):
    karte = create_map2(idvs, tilesV, GRIDSIZE)
    show_map(karte)
    if pos == anzTiles: return idvs
    for idv in tilesV:
      if idv[0] in ids: continue
      if match_tiles(pos, idv, idvs):
        if (solution := dfs(pos+1, idvs+[idv], ids | {idv[0]})): return solution
        karte = create_map2(idvs, tilesV, GRIDSIZE)
        show_map(karte)
  
  solution = dfs(0, [], set())
  karte = create_map(solution, tilesV, GRIDSIZE)
  pattern = '#[.#]{77}#....##....##....###[.#]{77}#..#..#..#..#..#'
  # 144 puzzel-teile ergeben eine GRDS von 12 * 8 Zeichen = 96-19 = 77

  for _, variante in rot_flip('a', karte):
    kartenStr = ''.join(variante)
    if (anz_monster := len(regex.findall(pattern, kartenStr, overlapped=True))):
      return kartenStr.count('#') - 15 * anz_monster

def show_map(karte):
  screen.fill((0,0,0))
  clock.tick(40)
  va = 0
  for y,zeile in enumerate(karte):
    ha = 0
    if y % 10 == 0: va +=AB
    for x, char in enumerate(zeile):
      if x % 10 == 0: ha +=AB 
      if char == '.':
        pg.draw.rect(screen,'#0F7833',(x*TS+ha, y*TS+va, TS, TS))
      else:
        pg.draw.rect(screen,'#CE1713',(x*TS+ha, y*TS+va, TS, TS))
  pg.display.flip()         

puzzle = read_puzzle('Tag_20.txt')
pg.init()
TS = 8
AB = 3
clock = pg.time.Clock()
screen = pg.display.set_mode((120*TS+13*AB, 120*TS+13*AB))


start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)