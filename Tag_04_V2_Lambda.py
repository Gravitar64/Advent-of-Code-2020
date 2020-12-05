import time
import re


def größe_gültig(s):
  hgt, einheit = int(s[:-2]), s[-2:]
  return einheit == 'cm' and (150 <= hgt <= 193) or \
      einheit == 'in' and (59 <= hgt <= 76)


req_fields = {'byr': lambda s: 1920 <= int(s) <= 2002,
              'iyr': lambda s: 2010 <= int(s) <= 2020,
              'eyr': lambda s: 2020 <= int(s) <= 2030,
              'hgt': größe_gültig,
              'hcl': lambda s: re.fullmatch(r'#[0-9a-f]{6}', s),
              'ecl': lambda s: s in 'amb blu brn gry grn hzl oth'.split(),
              'pid': lambda s: re.fullmatch(r'[0-9]{9}', s)}


def puzzle_einlesen(datei):
  with open(datei) as f:
    p1 = [zeile.replace('\n', ' ').split() for zeile in f.read().split('\n\n')]
    return [dict(eintrag.split(':') for eintrag in zeile) for zeile in p1]


def löse(puzzle):
  c1 = c2 = 0
  for d in puzzle:
    if len(d) == 8 or (len(d) ==7 and not "cid" in d):
      c1 += 1
      if all(func(d[k]) for k, func in req_fields.items()): 
        c2 += 1
  return c1,c2

puzzle = puzzle_einlesen('Tag_04.txt')
start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)