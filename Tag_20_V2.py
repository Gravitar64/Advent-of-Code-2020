import time
import math
import regex as re

def read_puzzle(file):
  with open(file) as f:
    return [[x for x in tile.split('\n')] for tile in f.read().split('\n\n')]

def rot_flip(id, tile):
  for i in range(4):
    yield (id,i), tile
    yield (id,i+4), tile[::-1] #flipV
    tile = list(map(''.join, zip(*tile[::-1]))) # rotate 90 degrees cw

def create_map(solution, tilesV, GRID_SIZE, TILE_SIZE):
  karte = []
  for start in range(0, len(solution), GRID_SIZE):
    for y in range(1, TILE_SIZE-1):
      zeile = ''
      for x in range(GRID_SIZE):
        zeile += tilesV[solution[start+x]][y][1:TILE_SIZE-1]
      karte.append(zeile)
  return karte      

def solve(puzzle):
  tiles = {tile[0][5:-1]: tile[1:] for tile in puzzle}
  anzTiles = len(tiles)
  GRID_SIZE = int(anzTiles ** 0.5)
  TILE_SIZE = len(puzzle[0][1])
  tilesV = {idv: variante for id, tile in tiles.items() for idv, variante in rot_flip(id, tile)}
  
  def match_tiles(pos, idV, placed_idvs):
    col, row = pos % GRID_SIZE, pos // GRID_SIZE
    matchV = row == 0 or tilesV[idV][0] == tilesV[placed_idvs[pos-GRID_SIZE]][-1]  
    matchH = col == 0 or [z[0] for z in tilesV[idV]] == \
                         [z[-1] for z in tilesV[placed_idvs[pos-1]]]
    return matchV and matchH    
  
  def dfs(pos,placed_idvs,seen_ids):
    if pos == anzTiles: return placed_idvs
    for idV in tilesV:
      if idV[0] in seen_ids: continue
      if match_tiles(pos, idV, placed_idvs):
        solution = dfs(pos+1, placed_idvs + [idV], seen_ids | {idV[0]})
        if solution: return solution
  
  solution = dfs(0,[],set())
  part1 = math.prod(int(idV[0]) for idV in [solution[0], solution[-1], solution[GRID_SIZE-1],solution[-GRID_SIZE]])
  
  karte = create_map(solution, tilesV, GRID_SIZE, TILE_SIZE)
  pattern = r'#[.#]{77}#....##....##....###[.#]{77}#..#..#..#..#..#'
  
  for idv, variante in rot_flip('a', karte):
    kartenStr = ''.join(variante)
    monsters = len(re.findall(pattern, kartenStr, overlapped=True))
    if monsters: return part1, kartenStr.count('#') - 15 * monsters

puzzle = read_puzzle('Tag_20.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)