import time, math, regex


def read_puzzle(file):
  with open(file) as f:
    return [[x for x in zeile.split('\n')] for zeile in f.read().split('\n\n')]


def rot_flip(id, tile):
  for i in range(4):
    yield (id, i), tile
    yield (id, i+4), tile[::-1]  # vertikal gespiegelt
    tile = list(map(''.join, zip(*tile[::-1]))) # rotiert um 90 Grad im Uhrzeigersinn


def create_map(sol, tilesV, GRDS):
  karte = ['']*len(sol)
  for pos, idv in enumerate(sol):
    puzzle_zeile = pos // GRDS
    for zeile in range(8):
      karte[puzzle_zeile*8+zeile] += tilesV[idv][zeile+1][1:9]
  return karte


def solve(puzzle):
  anzTiles = len(puzzle)
  GRDS = int(math.sqrt(anzTiles))
  tilesV = {idv: variante for tile in puzzle 
            for idv, variante in rot_flip(int(tile[0][5:-1]),tile[1:])}

  def match_tiles(pos, idv, idvs):
    spalte, zeile = pos % GRDS, pos // GRDS
    matchV = zeile == 0 or tilesV[idv][0] == tilesV[idvs[pos-GRDS]][-1]
    matchH = spalte == 0 or [z[0] for z in tilesV[idv]] == [
        z[-1] for z in tilesV[idvs[pos-1]]]
    return matchH and matchV

  def dfs(pos, idvs, ids):
    if pos == anzTiles: return idvs
    for idv in tilesV:
      if idv[0] in ids: continue
      if match_tiles(pos, idv, idvs):
        if (solution := dfs(pos+1, idvs + [idv], ids | {idv[0]})): return solution

  sol = dfs(0, [], set())
  part1 = math.prod(sol[i][0] for i in [0, -1, GRDS-1, -GRDS])

  karte = create_map(sol, tilesV, GRDS)
  pattern = r'#[.#]{77}#....##....##....###[.#]{77}#..#..#..#..#..#'
  # puzzle = 12 Teile * 8 = 96 - 19 = 77

  for _, variante in rot_flip('a', karte):
    kartenStr = ''.join(variante)
    if (monsters := len(regex.findall(pattern, kartenStr, overlapped=True))):
      return part1, kartenStr.count('#') - 15 * monsters


puzzle = read_puzzle('Tag_20.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)