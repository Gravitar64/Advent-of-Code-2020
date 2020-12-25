import time


def read_puzzle(file):
  with open(file) as f:
    return f.read().split('\n\n')


def solve(puzzle):
  p1 = [int(n) for n in puzzle[0].split('\n')[1:]]
  p2 = [int(n) for n in puzzle[1].split('\n')[1:]]

  while p1 and p2:
    a, b = p1.pop(0), p2.pop(0)
    if a > b:
      p1 += [a, b]
    else:
      p2 += [b, a]
  return sum([karte*(i+1) for i, karte in enumerate(reversed(p1 or p2))])


def solve2(puzzle):

  def sub_games(p1, p2):
    deckSet = set()
    while p1 and p2:
      if (decks := (tuple(p1), tuple(p2))) in deckSet:
        return 1
      else:
        deckSet.add(decks)
        a, b = p1.pop(0), p2.pop(0)
        if len(p1) >= a and len(p2) >= b:
          winner = sub_games(p1[:a], p2[:b])
        else:
          winner = 1 if a > b else 2
      if winner == 1:
        p1 += [a, b]
      else:
        p2 += [b, a]
    return winner

  p1 = [int(n) for n in puzzle[0].split('\n')[1:]]
  p2 = [int(n) for n in puzzle[1].split('\n')[1:]]
  sub_games(p1, p2)
  return sum([karte*(i+1) for i, karte in enumerate(reversed(p1 or p2))])


puzzle = read_puzzle('Tag_22.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(solve2(puzzle), time.perf_counter()-start)
