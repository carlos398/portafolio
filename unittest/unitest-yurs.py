import unittest
from ejercicio_yurs import order_by_age


users = [
    {'name': 'yurley', 'birthday': '1994-06-22' },
    {'name': 'mac-gr', 'birthday': '1993-08-31' },
    {'name': 'carlos', 'birthday': '2000-06-02' },
    {'name': 'reyezz', 'birthday': '1994-09-21' },
    {'name': 'dayana', 'birthday': '1992-12-27' },
    {'name': 'maximo', 'birthday': '2011-06-02' },
    {'name': 'manolo', 'birthday': '1997-01-26' }
]


users2 = [
    {'name': 'maximo', 'birthday': '2011-06-02'},
    {'name': 'carlos', 'birthday': '2000-06-02'},
    {'name': 'manolo', 'birthday': '1997-01-26'},
    {'name': 'reyezz', 'birthday': '1994-09-21'},
    {'name': 'yurley', 'birthday': '1994-06-22'},
    {'name': 'mac-gr', 'birthday': '1993-08-31'},
    {'name': 'dayana', 'birthday': '1992-12-27'}
]

class TestOrderAge(unittest.TestCase):
    def test_area(self):
        #Test area when radius >= 0
        print("test cunado conocemos el resultado")
        self.assertAlmostEqual(order_by_age(users), users2)
