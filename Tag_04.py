import time
import string


req_fields = 'ecl pid eyr hcl byr iyr hgt'.split()

def puzzle_einlesen(datei):
  with open(datei) as f:
    p1 = [zeile.replace('\n', ' ').split() for zeile in f.read().split('\n\n')]
    return [dict(eintrag.split(':') for eintrag in zeile) for zeile in p1]


def löse(puzzle):
  valid1 = []
  for d in puzzle:
    if all([x in d for x in req_fields]):
      valid1.append(d)
  return valid1


def löse2(valid1):
  counter = 0
  for d in valid1:
    if not(1919 < int(d['byr']) < 2003): continue
    if not(2009 < int(d['iyr']) < 2021): continue
    if not(2019 < int(d['eyr']) < 2031): continue
    hgt, einheit = int(d['hgt'][:-2]), d['hgt'][-2:]
    if einheit not in ('cm', 'in'): continue
    if einheit == 'cm' and not(149 < hgt < 194): continue
    if einheit == 'in' and not(58 < hgt < 77): continue
    if len(d['hcl']) != 7 or not(all(c in string.hexdigits for c in d['hcl'][1:])): continue
    if not d['ecl'] in 'amb blu brn gry grn hzl oth'.split(): continue
    if len(d['pid']) != 9 or not(all(c in string.digits for c in d['pid'])): continue
    counter += 1
  return counter


puzzle = puzzle_einlesen('Tag_04.txt')

start = time.perf_counter()
v1 = löse(puzzle)
print(len(v1), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(v1), time.perf_counter()-start)