from room import Room
from occupant import Occupant


class Amity:

    '''
    A class to model the Amity building which
    contains the various living and office spaces
    '''

    def __init__(self):
        self.office_rooms = []
        self.living_rooms = []
        self.boarding_fellows = []
        self.non_boarding_fellows = []
        self.staff = []
        # populate with model with rooms
        self.populate()
        # populate model with occupants
        self.create_occupants()

    def create_occupants(self):
        '''
        Reads occupant details from txt file
        and store them as occupant objects
        '''
        # read occupant's info from the occupants.txt file
        with open('data/occupants.txt', 'r') as doc:
            for line in doc.readlines():
                line = line.strip()
                if line:
                    details = line.split()
                    occupant1 = Occupant(name=details[0] + ' ' + details[1],
                                         job_type=details[2])
                    if details[2] == 'FELLOW':
                        if details[-1] == 'Y':
                            self.boarding_fellows.append(occupant1)
                        else:
                            self.non_boarding_fellows.append(occupant1)
                    else:
                        self.staff.append(occupant1)

    def allocate(self):
        '''
        Allocates spaces to fellows and staff
        input file
        '''
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

    def populate(self):
        '''
        Populates the building with 10 office
        spaces and 10 living spaces from the input
        file
        '''
        with open('data/rooms.txt') as rooms:
            for line in rooms.readlines():
                line = line.strip()
                if line:
                    name, usage = line.split(' ')
                    if usage == 'O':
                        space = Room(name=name, usage=usage, capacit=6)
                        self.office_rooms.append(space)
                    else:
                        space = Room(name=name, usage=usage, capacit=4)
                        self.living_rooms.append(space)
