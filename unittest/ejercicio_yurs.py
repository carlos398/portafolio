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


persons = [
    {'name': 'yurley', 'birthday': '1994-06-22' },
    {'name': 'mac-gr', 'birthday': '1993-08-31' },  
    {'name': 'carlos', 'birthday': '2000-06-02' },
    {'name': 'reyezz', 'birthday': '1994-09-21' },
    {'name': 'dayana', 'birthday': '1992-12-27' },   
    {'name': 'maximo', 'birthday': '2011-06-02' },
    {'name': 'manolo', 'birthday': '1997-01-26' }
]


def order_by_age(persons):
    """
    this function takes the dates and sorts them
    from oldest to youngest according to the age of the person.
    
    param
    persons: is the dictionary on line 15
    
    returns
    persons sorted
    """
    
    persons.sort(key=lambda p: p['birthday'],reverse=True)
    
    for i in persons:
        print(i)
    
    return persons


def person_birthd(person):
    """
    this function will help us to find the name and date of birth of each person. 

    parameters:

    person: will be the iterator through which we will go through the list.

    returns:

    person_birthday : date of birth of the person
    person_name : name of the person
    """
    
    person_birthday = person['birthday']
    person_birthday = datetime.datetime.strptime(person_birthday, '%Y-%m-%d')
    person_name = person['name']

    return person_birthday, person_name 


def other_person_birthd(other_person):
    """
    this function will help us to find the name and date of birth of each person. 

    parameters:

    other_person: will be the iterator through which we will go through the list.

    returns:

    other_person_birthday : date of birth of the person
    other_person_name : name of the person
    """
    
    other_person_birthday = other_person['birthday']
    other_person_birthday = datetime.datetime.strptime(other_person_birthday, '%Y-%m-%d')
    other_person_name = other_person['name']

    return other_person_birthday,other_person_name
    

def age_dif():
    """
    this function we are going to iterate in the dictionary people
    to look for first inside our function person_birthd the name and the date of birth of each person,
    then we will iterate again to compare one by one with each one of the people in the list,
    this with the motive to find the difference of time between one and the other. 
    """
    for person in persons:
        person_birthday, person_name = person_birthd(person)
        print('*'*50,' {person_name} '.format(person_name=person_name),'*'*50)
        for other_person in persons:
            other_person_birthday, other_person_name = other_person_birthd(other_person)
            rd = rdelta.relativedelta(person_birthday,other_person_birthday)
            print("the diference between {person_name} and {other_person_name} is: ".format(person_name=person_name, other_person_name=other_person_name))
            print('{0.years} years, {0.months} months and {0.days} days'.format(abs(rd)))
    return None    
    
if __name__ == "__main__":
    age_dif()