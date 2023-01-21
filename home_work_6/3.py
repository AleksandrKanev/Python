# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

li = (input('Ведите число: '))
li = list(filter(lambda x: not x == '.', li))
li = list(map(int,li))

print(sum(li))
