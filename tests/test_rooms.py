import unittest

from room import Room
from occupant import Occupant


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room(name='Valhalla', capacity=6, usage='OFFICE')

    def test_room_get_room_capacity(self):
        result = self.room.get_room_capacity()
        self.assertEqual(result, 6)

    def test_add_occupant_to_the_room(self):
        self.occupant1 = Occupant(name='Alex Kiura', job_type='fellow')
        self.room.add_occupant(self.occupant1)
        self.assertFalse(self.room.is_empty())

    def test_get_number_of_occupants(self):
        self.occupant1 = Occupant(name='Alex Kiura', job_type='fellow')
        self.room.add_occupant(self.occupant1)
        result = len(self.room.get_occupants())
        self.assertEqual(result, 1)
