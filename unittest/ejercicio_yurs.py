 
#!/usr/bin/myvenv python
# -*- coding: utf-8 -*-

import datetime
from dateutil import relativedelta as rdelta

"""
dictionary of values
send
key: name with a person's name
birthday: with the date of birth
"""


users = [
    {'name': 'yurley', 'birthday': '1994-06-22' },
    {'name': 'mac-gr', 'birthday': '1993-08-31' },
    {'name': 'carlos', 'birthday': '2000-06-02' },
    {'name': 'reyezz', 'birthday': '1994-09-21' },
    {'name': 'dayana', 'birthday': '1992-12-27' },
    {'name': 'maximo', 'birthday': '2011-06-02' },
    {'name': 'manolo', 'birthday': '1997-01-26' }
]

YEAR = ('year', 'years')
MONTH = ('month', 'months')
DAY = ('day', 'days')


def order_by_age(users):
    """
    This function takes the dates and sorts them
    from oldest to youngest according to the age of the person.
    param persons: is the dictionary on line 15
    returns
    persons sorted
    """

    users.sort(key=lambda p: p['birthday'], reverse=True)

    for i in users:
        print(i)

    return users


def get_birth_and_name(person):
    """
    This function will help us to find the name and date of birth of each person.
    parameters:
    other_person: will be the iterator through which we will go through the list.
    returns:
    other_person_birthday : date of birth of the person
    other_person_name : name of the person
    """

    other_person_birthday = person.get('birthday')
    other_person_birthday = datetime.datetime.strptime(other_person_birthday, '%Y-%m-%d')
    other_person_name = person.get('name')

    return other_person_birthday, other_person_name


def age_diff():
    """
    This function we are going to iterate in the dictionary people
    to look for first inside our function person_birth the name and the date of birth of each person,
    then we will iterate again to compare one by one with each one of the people in the list,
    this with the motive to find the difference of time between one and the other.
    """

    for person in users:
        person_birthday, person_name = get_birth_and_name(person)
        print('')
        print('*'*50, ' {person_name} '.format(person_name=person_name), '*'*50)
        for other_person in users:
            other_person_birthday, other_person_name = get_birth_and_name(other_person)
            rd = rdelta.relativedelta(person_birthday, other_person_birthday)
            print("the difference between {person_name} and {other_person_name} is: ".format(
                person_name=person_name,
                other_person_name=other_person_name
            ))
            print_diff(rd)


def print_diff(rd):
    """
    Show difference values form relative date
    :param rd:  Obj Relative Ie, <1 years, 2 months, 4 days>
    :return:  7 years 5 months 6 days
    """

    msj_year = get_format_date(rd.years, YEAR)
    msj_month = get_format_date(rd.months, MONTH)
    msj_day = get_format_date(rd.days, DAY)
    message = '{}{}{}'.format(msj_year, msj_month, msj_day)

    print(message)

    return message


def get_format_date(segment, nomenclatures):
    """
    Define structure to show segment of date
    :param segment: Number of secgment date (years, month or day) Ie, 12
    :param nomenclatures: Tuple of String define piece of nomeclature Ie, (year, years)
    :return: String message Ie, '14 years 4 months 7 days '
    """
    message = ''
    if segment != 0:
        nomenclature = nomenclatures[1]
        if abs(segment) == 1:
            nomenclature = nomenclatures[0]
        message = '{} {} '.format(
            abs(segment),
            nomenclature
        )
    return message


if __name__ == "__main__":
    order_by_age(users)