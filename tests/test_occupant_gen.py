import unittest
from occupant_gen import Occupants


class OccupantGenTest(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 2, 4, 5, 6]
        self.number_gen = Occupants.next(self.numbers)

    def test_occupant_gen_first_generation(self):
        # restart the generator
        self.number_gen = None
        self.number_gen = Occupants.next(self.numbers)
        self.assertEqual(sum(self.numbers),
                         sum(list(self.number_gen)))
