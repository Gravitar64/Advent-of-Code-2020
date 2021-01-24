from collections import defaultdict
import time
import math
import regex


def read_puzzle(file):
  with open(file) as f:
    return [[x for x in zeile.split('\n')] for zeile in f.read().split('\n\n')]


def rot_flip(id, tile):
  for i in range(4):
    yield (id, i), tile
    yield (id, i+4), tile[::-1]  # vertikal gespiegelt
    tile = list(map(''.join, zip(*tile[::-1]))) # rotiert um 90 Grad im Uhrzeigersinn


def create_map(solution, tilesV, GRDS):
  karte = defaultdict(str)
  for pos, idv in enumerate(solution):
    puzzle_zeile = pos // GRDS
    for zeile in range(8):
      karte[puzzle_zeile*8+zeile] += tilesV[idv][zeile+1][1:9]
  return list(karte.values())


def solve(puzzle):
  tiles = {int(tile[0][5:-1]): tile[1:] for tile in puzzle}
  anzTiles = len(tiles)
  GRDS = int(math.sqrt(anzTiles))
  tilesV = {idv: variante for id, tile in tiles.items()
            for idv, variante in rot_flip(id, tile)}

  def match_tiles(pos, idv, placed_idvs):
    spalte, zeile = pos % GRDS, pos // GRDS
    matchH = spalte == 0 or [z[0] for z in tilesV[idv]] == [
        z[-1] for z in tilesV[placed_idvs[pos-1]]]
    matchV = zeile == 0 or tilesV[idv][0] == tilesV[placed_idvs[pos-GRDS]][-1]
    return matchH and matchV

  def dfs(pos, placed_idvs, seen_ids):
    if pos == anzTiles: return placed_idvs
    for idv in tilesV:
      if idv[0] in seen_ids: continue
      if match_tiles(pos, idv, placed_idvs):
        solution = dfs(pos+1, placed_idvs + [idv], seen_ids | {idv[0]})
        if solution: return solution

  sol = dfs(0, [], set())
  part1 = math.prod(idv[0] for idv in [sol[0], sol[-1], sol[GRDS-1], sol[-GRDS]])

  karte = create_map(sol, tilesV, GRDS)
  pattern = r'#[.#]{77}#....##....##....###[.#]{77}#..#..#..#..#..#'
  # puzzle = 12 Teile * 8 = 96 - 19 = 77

  for idv, variante in rot_flip('a', karte):
    kartenStr = ''.join(variante)
    monsters = len(regex.findall(pattern, kartenStr, overlapped=True))
    if monsters:
      return part1, kartenStr.count('#') - 15 * monsters


puzzle = read_puzzle('Tag_20.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)
