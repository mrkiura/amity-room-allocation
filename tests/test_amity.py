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

    def test_print_allocated(self):
        self.assertEqual(len(self.building.print_allocated()), 100)

    def test_analyse_allocations(self):
        result = self.building.analyze_allocations()
        self.assertTrue('total rooms' in result)
        self.assertTrue('allocated rooms' in result)
        self.assertTrue('total occupants' in result)
        self.assertEqual(result['total rooms'], 20)
        self.assertEqual(result['total occupants'], 114)
        self.assertEqual(result['allocated occupants'], 100)
