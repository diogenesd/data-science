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


def hours2days(time_hour):
    """ this function transform o time in days.

        Função hours2days que tenha um argumento, um número inteiro,
        que é um período de tempo em horas.
        A função deve retornar uma tupla de quanto tempo esse período
        é em dias e horas, sendo as horas
        o restante que não pode ser expresso em dias.

        Args:
            time_hour (int): tempo em horas.

        Returns:
           tupla: função retorna uma tupla de quanto tempo
           esse período é em dias e horas.

        """
    assert time_hour > 0
    return time_hour // 24, time_hour % 24


print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))


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


def convert_to_numeric(score):
    """
    Converte a pontuação para um tipo numérico.
    """
    converted_score = int(score)
    return converted_score
