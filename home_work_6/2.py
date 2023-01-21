#  Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

li = [12,'sadf',5643]

li_1 = list((i) for i in li if type(i) == str)
li_2 = list(filter(lambda x: type(x) == int, li))

print(li_1, li_2)