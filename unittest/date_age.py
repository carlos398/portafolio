#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from dateutil import relativedelta as rdelta


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
    date_birthday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
    rd = rdelta.relativedelta(date_now, date_birthday)
    age = rd.years

    return '{age} years'.format(age=age)


if __name__ == '__main__':
    birthday = get_birthday()
    print('birthday', birthday)
    age = get_age(birthday)
    print('you age is: {age}'.format(age=age))