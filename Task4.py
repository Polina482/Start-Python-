# a = [1,1.1, 'a',[1],(1,1.1), {1,2},{'a':1},None, True] #Список в котором: целое; вещественное; строковое; другой список; кортеж; множество; словарь; пустой тип; булевый тип.
# a =[] # Пустой список
# b = list() # Пустой список
# a = (1,2.1,3) # Раньше я был кортежем
# list(a) # [1,2.1,3], но 'a' остался кортежем
# b = list('abc') # ['a','b','c']
# a = [1,1.1,'a']
# print(a) # [1,1.1,'a']
# print ([1,1.1,'a']) # [1,1.1,'a']
# a = [1,1.1,'a']
# a[0] # 1
# a[1] # 1.1
# a[2] #'a'
# a[3] # Ошибка, вышли за гарницы
# a[-1] # 'a'
# a[-2] # 1.1
# a[-3] #1
# a[-4] # Ошибка, вышли за границы
# a = [1,2,3]
# a.index(3) #2. Возвращаем индекс, где передоваемое значение состоит в списке. В примере вернется 2, так как значение 3 в списке состоит на 2-ом индексе.
# a = [1,1 1.1, 'a']
# a[0] = 'a' # Теперь 'a' равно ['a',1.1,'a']
# a[1] = 'б' # Теперь 'a' равно ['a', 'б', 'a']
# a[-1] = 'в' # Теперь 'a' равно ['a', 'б', 'в']
# a = [1,2,3] # Теперь 'a' равно [1,2,3]
# a = [1,2,3]
# a.append(4) # Добавляет значение (объектов) в конце списка. Добавляет только один объект или значение. Теперь "a" [1,2,3,4]
# a.append(['a','b'])
# a = [1,2,3]
# a.insert(3,4)
# a = [1,2,3]
# a.insert(-1,4)
# a = [1,2,3]
# a.extend([4,5,6])
# a = [1, 1.1, 1, 'a']
# del a[0]
# del a[-1]
# del a[-1]
# del a
# a = [1,2,2]
# a.clear()
# a = [1,2,3]
# a.pop()
# a = [1, 'ab', 3]
# a.pop(1)
# a= [1,2, 'ab']
# a.remove('ab')
# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)
# a + = b
# a = [1,2,3]
# b = 2
# c = a * b
# print(c)
# a *= b
# a = [1,2,3]
# b = [[1,2,3], [4,5,6], [7,8,9]]
# b = [[1,2,3], [4,5,6,], [7,8,9]]
# b[0]
# b[0][0]
# b[-1][-1]


# # ЗАДАЧА 1
a = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38,-92, -45, 67, 53, 25]
b = len(a)
print (b)
c = [2, -93, -2, 8, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
d = sum(c)
e  = d // 19
print(e)
a[4] = -17
print(a)


# # Задача 2
# list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# b = len(list_playrs)
# print(b)
# #b [start : step : stop]
# print (list_players[0:3])
# print (list_players[3:6])


# ЗАДАЧА 3
##1
# mails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
# emails = mails [: : -1]
# print (emails)
##2
# mails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
# mails. reverse()
#print (mails)
emails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
print ('Третье письмо:',)
print ('Предпоследнее письмо:',)


# ## Задача 5
# results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]
# a = sum(results)
# b = len(results)
# c = a//b
# print (c)
# min_score =min(results)
# max score = max(results)
# print(min_score)
# print(max_score)

# ## Задача 6
# fruits = ["яблоко", "банан", "опельсин", "виноград"]
# fruits[2] = 'апельсин'
# print(fruits)


# ## Задача7
# speed = 4096 / 1024
# time = 120 * 60
# coast = 0.125
# free = 500
#





