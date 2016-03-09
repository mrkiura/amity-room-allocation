from room import Room


class Amity:

    '''
    A class to model the Amity building which
    contains the various living and office spaces
    '''

    def __init__(self):
        self.rooms = []

    def allocate(self, people):
        '''
        Allocates spaces to the people included in the
        input file
        '''
        self.allocations = []
        pass

    def get_available_rooms(self):
        '''
        Returns a list of rooms with spaces
        '''
        available = []
        for i in self.rooms:
            if not i.is_full():
                available.append(i)
        return available

    def get_allocations(self):
        '''
        Returns a list of rooms and the
        people allocated to that room
        '''
        return self.allocations

    def populate(self, rooms):
        '''
        Populates the building with 10 office
        spaces and 10 living spaces from the input
        file
        '''
