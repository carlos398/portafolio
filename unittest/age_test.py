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
        self.assertEqual(age, 27)
