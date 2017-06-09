import unittest

"""
DocString for .

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: TimeDelta

"""


def readable_timedelta(days):
    """ This funcition transform days to weeks.

            Keyowrds argumnets:
            days: int. Amount of days to transform in weeks and days.

            return: Amount of days weeks and days.

            """
    assert days > 0
    # Weeks is the return integer number of the division by seven
    # Days is the return module number of the division by seven

    return "{} week(s) and {} day(s).".format(days // 7, days % 7)


how_many_snakes = 1
snake_string = """
Bem-vindo ao Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Philip e Charlie
"""


print(snake_string * how_many_snakes)


class TestVolumeCilindrico(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(readable_timedelta(10), "1 week(s) and 3 day(s).")
        self.assertEqual(readable_timedelta(1), "0 week(s) and 1 day(s).")

    def test_not_equals(self):
        self.assertNotEqual(readable_timedelta(2), "0 week(s) and 1 day(s).")
        self.assertNotEqual(readable_timedelta(1), "0 week(s) and 10 day(s).")


if __name__ == '__main__':
    unittest.main()
