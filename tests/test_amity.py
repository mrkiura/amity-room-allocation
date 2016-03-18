import unittest
from amity import Amity


class AmityTest(unittest.TestCase):

    def setUp(self):
        self.building = Amity()

    def tearDown(self):
        self.building = None

    def test_populate_offices(self):
        '''
        Test whether the populate method
        populates the building with office rooms
        '''
        self.assertTrue(len(self.building.office_rooms), 10)

    def test_populate_living(self):
        '''
        Test whether the populate method
        populates the building with living rooms
        '''
        self.assertEqual(len(self.building.living_rooms), 10)

    def test_create_staff(self):
        '''
        Test create_occupants method
        '''
        self.assertEqual(len(self.building.staff), 32)

    def test_create_fellows(self):
        '''
        Test create_occupants method
        '''
        fellows = len(self.building.boarding_fellows +
                      self.building.non_boarding_fellows)
        self.assertEqual(fellows, 82)

    def test_allocate(self):
        '''
        Tests allocate method
        '''
        self.assertEqual(len(self.building.get_allocations()), 20)

    def test_get_available_room(self):
        '''
        Tests getting available rooms
        '''
        self.assertEqual(len(self.building.get_available_rooms('LIVING')), 0)

    def test_get_unallocated(self):
        '''
        Tests getting unallocated staff
        '''
        self.assertTrue(
            len(self.building.get_unallocated_occupants()), 38)
