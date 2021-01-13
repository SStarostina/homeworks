# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_2 or arg_1 >= arg_3:
        a = arg_1
        if arg_2 >= arg_3:
            b = arg_2
        else:
            b = arg_3
    else:
        a = arg_3
        b = arg_2

    c = a + b
    return c

result = my_func(1, 5, 0)

print(f'Сумма чисел: {result} ')
