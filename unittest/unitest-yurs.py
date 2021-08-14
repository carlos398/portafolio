import unittest
from ejercicio_yurs import order_by_age


users = [
    {'name': 'pedro', 'birthday': '1990-06-22' },
    {'name': 'ana', 'birthday': '1995-08-31' },
    {'name': 'juancho', 'birthday': '2020-06-02' },
    {'name': 'guacho', 'birthday': '2004-09-21' },
    {'name': 'king', 'birthday': '2005-12-27' },
    {'name': 'dos', 'birthday': '2001-06-02' },
    {'name': 'rick', 'birthday': '1997-01-26' }
]


users2 = [
    {'name': 'juancho', 'birthday': '2020-06-02' },
    {'name': 'king', 'birthday': '2005-12-27' },
    {'name': 'guacho', 'birthday': '2004-09-21' },
    {'name': 'dos', 'birthday': '2001-06-02' },
    {'name': 'rick', 'birthday': '1997-01-26' },
    {'name': 'ana', 'birthday': '1995-08-31' },
    {'name': 'pedro', 'birthday': '1990-06-22' },
]

class TestOrderAge(unittest.TestCase):
    def test_area(self):
        #Test area when radius >= 0
        print("test cunado conocemos el resultado")
        self.assertAlmostEqual(order_by_age(users), users2)
