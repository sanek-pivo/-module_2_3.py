my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = len(my_list)
o = 0
while o <= number:
    print(my_list[o])
    o = o + 1
    if my_list[o] < 0:
        break  #прерывание цикла
    elif my_list[o] == 0:
        o > number
        o = o + 1
        continue  #переход в начало цикла

