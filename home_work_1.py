# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# day = int(input('Введите день недели: '))
# if 5 < day < 8:
#     print('да')
# elif 0 < day < 6:
#     print('нет')
# else:
#     print('в неделе 7 дней')

# 2)Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            print(i, j, k)
            print(not (i or j or k) == (not i and not j and not k))

# 3)Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите Х: '))
# y = int(input('Введите Y: '))

# if x == 0 or y == 0:
#     print('Введите цифру отличное от нуля')
# elif x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# x = int(input('Введите номер четверти: '))

# if x < 1 and x > 4:
#     print('Не существует такой четверти')
# elif x == 1:
#     print('x > 0, y > 0')
# elif x == 2:
#     print('x < 0, y > 0')
# elif x == 3:
#     print('x < 0, y < 0')
# else:
#     print('x > 0, y < 0')

# 5)Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# ax = float(input('Введите координаты точки a по оси x:'))
# ay = float(input('Введите координаты точки a по оси y:'))
# bx = float(input('Введите координаты точки b по оси x:'))
# by = float(input('Введите координаты точки b по оси y:'))

# distans = ((ax-bx)**2+(ay-by)**2) ** 0.5
# print(f'Растояние между точкой A до точки B = {distans}')
