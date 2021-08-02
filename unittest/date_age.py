#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def validate_patter(date_text, patter):
    """
    Validate string with specific patters
    :param date_text: String date to validae, Ie. '22/06/1994'
    :param patter: String patter to match, Ie. '%d/%m/%Y'
    :return: Bool valid if match with patter. Ie. True
    """

    try:
        datetime.datetime.strptime(date_text, patter)
        return True
    except ValueError:
        return False


def get_birthday():
    """
    Inteface to get information by console imputs
    :return: Int year of birth, Ie. 1994
    """

    flag = False
    while not flag:
        chair = "Digite su fecha de birthday en el formato: 'dd/mm/aaaa': "
        date_user = input(chair)
        flag = validate_patter(date_user, '%d/%m/%Y')

    return date_user


def get_age(birthday):
    """
    Calculate date
    :param birthday: String, date of birth dd/mm/yyyy, Ie. '22/06/1994'
    :return: 27 years
    """

    date_now = datetime.datetime.now()
    date_now_str = datetime.datetime.strftime(date_now, '%d/%m/%Y')
    year = str(date_now_str[-4:])
    mont_birthday = str(birthday[3:5])
    day_birthday  = str(birthday[0:2])

    mont_year = str(date_now_str[3:5])
    day_year = str(date_now_str[0:2])

    age = int(year) - int(birthday[-4:])

    if int(mont_birthday) > int(mont_year):
        age = age - 1
    elif int(day_birthday) > int(day_year) and int(mont_birthday) > int(mont_year):
        age = age - 1

    return '{age} years'.format(age=age)


if __name__ == '__main__':
    birthday = get_birthday()
    print('birthday', birthday)
    age = get_age(birthday)
    print('you age is: {age}'.format(age=age))