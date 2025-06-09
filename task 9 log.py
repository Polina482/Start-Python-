# ЗАДАЧА ПРИМЕР 1
print(f'Пример 1')
for x in 0, 1:
  for y in 0, 1:
      for z in 0, 1:
         for w in 0, 1:
                F = (x or y) and not (y == z) and not(w)
                if F == 1:
                    print(x, y, z, w, F)


print(f'Пример 2')
for a in 0, 1:
  for b in 0, 1:
      for c in 0, 1:
         F = (not(a or b)) and c
         if F == 1:
                print(a, b, c, F)

print(f'Пример 3')
for a in 0, 1:
  for b in 0, 1:
      for c in 0, 1:
         F = (not(a or b)) and c
         if F == 1:
                print(a, b, c, F)
