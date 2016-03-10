from room import Room
from occupant import Occupant


class Amity:

    '''
    A class to model the Amity building which
    contains the various living and office spaces
    '''

    def __init__(self):
        self.rooms = []
        # populate the class model on instantiation
        self.populate()
        # import ipdb
        # ipdb.set_trace()

    def allocate(self):
        '''
        Allocates spaces to the people included in the
        input file
        '''
        # read occupant's info from the occupants.txt file
        for line in open('data/occupants.txt'):
            line = line.strip()
            fname, lname, job_type, boarding = line.split(' ')
            if boarding == 'Y':
                boarding = True
            else:
                boarding = False
            occupant1 = Occupant(name=fname+' ' + lname,
                                 job_type=job_type, boarding=boarding)


        self.allocations = []

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

    def populate(self):
        '''
        Populates the building with 10 office
        spaces and 10 living spaces from the input
        file
        '''
        for line in open('data/rooms.txt'):
            line = line.strip()
            name, usage = line.split(' ')
            if usage == 'O':
                usage = 'OFFICE'
                capacity = 6
            else:
                usage = 'LIVING'
                capacity = 4
            space = Room(name=name, usage=usage, capacity=capacity)
            self.rooms.append(space)
