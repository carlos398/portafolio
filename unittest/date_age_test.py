#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import datetime
from date_age import get_age, validate_patter


class TestAge(unittest.TestCase):
    """
    Generate
    """

    def test_get_age(self):
        """
        Validate to age is 21
        """
        friends = {
            'mac': {
                'age': 27,
                'birthday': '31/08/1993',
            },
            'carlos': {
                'age': 21,
                'birthday': '02/06/2000',
            },
            'yurley': {
                'age': 27,
                'birthday': '22/06/1994',
            },
            'reyez': {
                'age': 26,
                'birthday': '21/09/1994',
            }
        }

        for key, values in friends.iteritems():
            birthday = values['birthday']
            base_age = values['age']
            age = get_age(birthday)

            self.assertEqual(age, '{} years'.format(base_age))


    def test_validate_patters(self):
        """
        Validate patters
        """

        is_valid = validate_patter('22/06/1994', '%d/%m/%Y')
        self.assertEqual(is_valid, True)

        is_valid = validate_patter('22/6/1994', '%d/%m/%Y')
        self.assertEqual(is_valid, True)

        is_valid = validate_patter('31/02/1994', '%d/%m/%Y')
        self.assertEqual(is_valid, False)

        is_valid = validate_patter('06/22/1994', '%m/%d/%Y')
        self.assertEqual(is_valid, True)

        is_valid = validate_patter('06/22/1994', '%d/%m/%Y')
        self.assertEqual(is_valid, False)

        is_valid = validate_patter('Hola Carlos', '%d/%m/%Y')
        self.assertEqual(is_valid, False)
