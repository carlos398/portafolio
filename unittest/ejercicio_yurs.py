#!/usr/bin/myvenv python
# -*- coding: utf-8 -*-

import datetime
from dateutil import relativedelta as rdelta

"""
diccionario de valores
envia
key: nombre con el nombre de una persona
birthday con la fecha de nacimiento
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
    this function takes the dictionary and serach the age of every one
    based on his birthday
     
    """
    
    persons.sort(key=lambda p: p['birthday'],reverse=True)
    
    for i in persons:
        print(i)
    
    return persons


def age_diference(persons):
    
    for person in persons:
        person_birthday = person['birthday']
        person_date_birthday = datetime.datetime.strptime(person_birthday, '%Y-%m-%d')
        person_name = person['name']
        print("*"*50, " {name} ".format(name=person_name),"*"*20)
        
        for other_person in persons:
            other_person_birthday = other_person['birthday']
            other_person_date_birthday = datetime.datetime.strptime(other_person_birthday, '%Y-%m-%d')
            other_person_name = other_person['name']
            rd = rdelta.relativedelta(person_date_birthday, other_person_date_birthday)
            dif = rd.years
            print("the diference betwen {name_person} and {name_persons_aroud} is {dif}".format(
                name_person=person_name, 
                dif=dif, 
                name_persons_aroud=other_person_name
            ))
            
            
if __name__ == "__main__":
    age_diference(persons)