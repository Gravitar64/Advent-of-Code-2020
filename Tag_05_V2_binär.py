#Idee von Brother Lui
import time

start = time.perf_counter()

S = set(int(s.translate({70:48,66:49,76:48,82:49}), 2) for s in open("Tag_05.txt"))
print(max(S), set(range(min(S), max(S))) - S)

print(time.perf_counter()-start)