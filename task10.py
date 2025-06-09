print(f'ЗАДАЧА 1')

from itertools import permutations
table = '457 567 45 136 123 247 126'.split()
graph = 'EF FA AB BG GE EC CB CD DF DA'.split()
print(*range(1, 8))
for p in permutations('ABCDEFG'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)


print(f'ЗАДАЧА 2')
from itertools import permutations
table = '234 157 147 138 268 54 23 456'.split()
graph = 'AF FH HC CB BD DG GA EB ED EH GF'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 3')
from itertools import permutations
table = '268 134678 257 27 38 12 234 125'.split()
graph = 'АГ ГБ БД ДИ ИЖ ЖЕ ЕВ ВА ГВ ГЕ ГИ ГД'.split()
print(*range(1, 9))
for p in permutations('АБВГДЖИЕ'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 4')

from itertools import permutations
table = '47 345 27 1267 268 458 134 56'.split()
graph = 'АБ БГ ГД ДИ ИЖ ЖЕ ЕВ ВА ГА ГЕ ДЖ'.split()
print(*range(1, 9))
for p in permutations('АБВГДЖИЕ'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 5')

from itertools import permutations
table = '23467 1356 12458 13 238 127 16 35'.split()
graph = 'AB BD DE EF FG GH HC CA DC CD DG GE CG'.split()
print(*range(1, 9))
for p in permutations('ABCDEFHG'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 6')

from itertools import permutations
table = '247 148 578 126 38 47 136 235'.split()
graph = 'AB BH HF FD DC CE EA AH GE GC GF'.split()
print(*range(1, 9))
for p in permutations('ABCDEFHG'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 7')

from itertools import permutations
table = '347 3456 1245 1237 236 25 14'.split()
graph = 'AB BC CE EG GF FD DA AC ED EF'.split()
print(*range(1, 8))
for p in permutations('ABCDEFG'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 8')

from itertools import permutations
table = '279 13789 2578 57 3468 589 1234 2356 126'.split()
graph = 'АБ БЖ ЖК КЗ ЗД ДА АВ АГ ВГ ВЖ ВЕ ГЕ ЖЕ ЗЕ КЕ ГД'.split()
print(*range(1, 10))
for p in permutations('АБВГДЕЖЗК'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)

print(f'ЗАДАЧА 9')

from itertools import permutations
table = '457 37 267 1678 16 3458 12348 467'.split()
graph = 'АБ БД ДЕ ЕЗ ЗГ ГА АВ ВД ДЖ ЖГ ЖВ ЕГ'.split()
print(*range(1, 9))
for p in permutations('АБВГДЕЖЗ'):
   if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
      print(*p)













