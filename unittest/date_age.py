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
        chair = "Digite su fecha de nacimiento en el formato: 'dd/mm/aaaa': "
        date_user = input(chair)
        flag = validate_patter(date_user, '%d/%m/%Y')

    return date_user


def get_age(nacimiento):
    """
    Calculate date
    :param nacimiento: String, date of birth dd/mm/yyyy, Ie. '22/06/1994'
    :return: 27 years
    """

    fechaActual = datetime.datetime.now()
    fechaActual2 = datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
    fechaActual2 = str(fechaActual2[-4:])
    edad = int(fechaActual2) - int(nacimiento[-4:])

    return '{} years'.format(edad)


if __name__ == '__main__':
    nacimiento = get_birthday()
    print('birthday', nacimiento)
    age = get_age(nacimiento)
    print('you age is: {age}'.format(age=age))