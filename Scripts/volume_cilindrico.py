import unittest

"""
DocString for volume_cilindrico.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Volume cilindrico

"""


def cylinder_volume(height, radius):
    """ Cylinder volume calculation. This function receive two parameters,
        the first is the height of the cylinder and second is the radius.
        The formula is height multiplication by number pi,
        and multiplication by square of the radius.

        Keyword arguments:
        height: int or float. The height of the cylinder.
        radius: int or float. The radius of the cylinder.

        return: float. Number containg the volume

    """

    pi = 3.14159
    return height * pi * radius ** 2


class TestVolumeCilindrico(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(cylinder_volume(10, 3), 282.7431)
        self.assertEqual(cylinder_volume(10, 2), 125.6636)
        self.assertEqual(cylinder_volume(10, 1), 31.4159)
        self.assertEqual(cylinder_volume(2, 2), 25.13272)

    def test_not_equals(self):
        self.assertNotEqual(cylinder_volume(2, 2), 0)
        self.assertNotEqual(cylinder_volume(10, 3), 9999999)


if __name__ == '__main__':
    unittest.main()
