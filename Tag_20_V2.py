import time
import math
import regex as re
from collections import defaultdict


def read_puzzle(file):
  with open(file) as f:
    return [[x for x in tile.split('\n')] for tile in f.read().split('\n\n')]


def rot_flip(id, tile):
  for i in range(4):
    yield (id, i), tile
    yield (id, i+4), tile[::-1]  # flipV
    tile = list(map(''.join, zip(*tile[::-1])))  # rotate 90 degrees cw


def create_map(solution, tilesV, GRDS):
  karte = defaultdict(str)
  for pos, idV in enumerate(solution):
    tile_row = pos // GRDS
    for zeile in range(8):
      karte[tile_row*8+zeile] += tilesV[idV][zeile+1][1:9]
  return list(karte.values())


def solve(puzzle):
  tiles = {int(tile[0][5:-1]): tile[1:] for tile in puzzle}
  anzTiles = len(tiles)
  GRDS = int(anzTiles ** 0.5)
  tilesV = {idv: variante for id, tile in tiles.items()
            for idv, variante in rot_flip(id, tile)}

  def match_tiles(pos, idV, placed_idvs):
    col, row = pos % GRDS, pos // GRDS
    matchV = row == 0 or tilesV[idV][0] == tilesV[placed_idvs[pos-GRDS]][-1]
    matchH = col == 0 or [z[0] for z in tilesV[idV]] == [
        z[-1] for z in tilesV[placed_idvs[pos-1]]]
    return matchV and matchH

  def dfs(pos, placed_idvs, seen_ids):
    if pos == anzTiles:
      return placed_idvs
    for idV in tilesV:
      if idV[0] in seen_ids:
        continue
      if match_tiles(pos, idV, placed_idvs):
        if (sol := dfs(pos+1, placed_idvs + [idV], seen_ids | {idV[0]})):
          return sol

  sol = dfs(0, [], set())
  part1 = math.prod(idV[0]
                    for idV in [sol[0], sol[-1], sol[GRDS-1], sol[-GRDS]])

  karte = create_map2(sol, tilesV, GRDS)
  pattern = r'#[.#]{77}#....##....##....###[.#]{77}#..#..#..#..#..#'

  for idv, variante in rot_flip('a', karte):
    kartenStr = ''.join(variante)
    monsters = len(re.findall(pattern, kartenStr, overlapped=True))
    if monsters:
      return part1, kartenStr.count('#') - 15 * monsters


puzzle = read_puzzle('Tag_20.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)