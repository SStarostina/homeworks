# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, year, city, mail, tel):
    print(f'имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {mail}, телефон: {tel}')

user('Иван', 'Воробьев', '1972', 'Краснодар', 'srt@mail.ru', '+78211552211')

# или

def info(**kwargs):
    return f'имя: {kwargs["name"]}, фамилия: {kwargs["surname"]}, год рождения: {kwargs["year"]}, город проживания: {kwargs["city"]}, email: {kwargs["mail"]}, телефон: {kwargs["tel"]}'

print(info(name='Иван', surname='Воробьев', year=1972, city='Краснодар', mail='srt@mail.ru', tel='+78211552211'))
