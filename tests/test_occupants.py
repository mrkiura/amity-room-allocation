import unittest

from occupant import Occupant
from room import Room


class OccupantsTest(unittest.TestCase):
    def setUp(self):
        self.occupant = Occupant(name='Alex Kiura', job_type='fellow')

    def test_occupant_get_job_type_result(self):
        result = self.occupant.get_job_type()
        self.assertEqual(result, 'fellow')
        
