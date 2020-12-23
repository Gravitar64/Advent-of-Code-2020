import time
import math
import regex as re


def read_puzzle(file):
  with open(file) as f:
    return [[x for x in tile.split('\n')]for tile in f.read().split('\n\n')]


def get_vars(id, tile):
  for i in range(4):
    yield (id, i), tile
    yield (id, i+4), [zeile for zeile in reversed(tile)]  # flipH
    tile = list(map("".join, zip(*tile[::-1])))  # rotate 90 cw


def get_border(tile, r):
  if r == 'u': return tile[0]
  if r == 'd': return tile[-1]
  if r == 'l': return ''.join([zeile[0] for zeile in tile])
  if r == 'r': return ''.join([zeile[-1] for zeile in tile])


def create_map(solution, tilesV, size):
  karte = []
  for start in range(0, len(solution), size):
    for y in range(1, 9):
      zeile = ''
      for offsX in range(size):
        zeile += tilesV[solution[start+offsX]][y][1:9]
      karte.append(zeile)
  return karte


def solve(puzzle):
  tiles = {tile[0][5: -1]: tile[1:] for tile in puzzle}
  tilesV = {idv: tile_v for id, tile in tiles.items()
            for idv, tile_v in get_vars(id, tile)}
  SIZE = int(len(tiles)**0.5)

  def match_tiles(pos, idV, order):
    matchH = pos % SIZE == 0 or get_border(
        tilesV[idV], 'l') == get_border(tilesV[order[-1]], 'r')
    matchV = pos < SIZE or get_border(
        tilesV[idV], 'u') == get_border(tilesV[order[-SIZE]], 'd')
    return matchH and matchV

  def dfs(placed_tiles, seen):
    if len(placed_tiles) == len(tiles):
      return placed_tiles
    pos = len(placed_tiles)
    for idV in tilesV:
      if idV[0] in seen:
        continue
      if match_tiles(pos, idV, placed_tiles):
        solution = dfs(placed_tiles + [idV], seen | {idV[0]})
        if solution:
          return solution

  solution = dfs([], set())
  part1 = math.prod(int(s[0]) for s in [solution[0],
                                        solution[-1], solution[SIZE-1], solution[-SIZE]])

  spacing = f'[.#\n]{{{SIZE*8-19}}}'
  monster = f'#.{spacing+"#....#"*3}##{spacing}.#{"..#"*5}'
  karte = create_map(solution, tilesV, SIZE)

  for _, karteV in get_vars('a', karte):
    karteStr = '\n'.join(karteV)
    if (monsters := len(re.findall(monster, karteStr, overlapped=True))):
      return part1, sum(x == '#' for x in karteStr) - 15*monsters


puzzle = read_puzzle('Tag_20.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)
