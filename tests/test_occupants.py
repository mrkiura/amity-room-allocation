import unittest

from occupant import Occupant
from room import Room


class OccupantsTest(unittest.TestCase):
    def test_occupant_creation(self):
        result = Occupant(name='Alex Kiura', job_type='fellow')
        self.assertIsInstance(result, Occupant)
