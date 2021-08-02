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

    date_now_list = date_now_str.split('/')
    day_now = int(date_now_list[0])
    month_now = int(date_now_list[1])
    year_now = int(date_now_list[2])

    birthday_list = birthday.split('/')
    day_birthday = int(birthday_list[0])
    month_birthday = int(birthday_list[1])
    year_birthday = int(birthday_list[2])

    age = year_now - year_birthday

    if month_birthday > month_now:
        # TODO: what happen if date is  05/08/2000 is the same month ...
        age = age - 1

    return '{age} years'.format(age=age)


if __name__ == '__main__':
    birthday = get_birthday()
    print('birthday', birthday)
    age = get_age(birthday)
    print('you age is: {age}'.format(age=age))