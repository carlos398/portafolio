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

        age = get_age(1993)
        self.assertEqual(age, 28)


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
