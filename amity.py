from room import Room
from occupant import Occupant
from occupant_gen import Occupants


class Amity(object):

    '''
    A class to model the Amity building which
    contains the various living and office spaces
    '''
    office_rooms = []
    living_rooms = []
    boarding_fellows = []
    non_boarding_fellows = []
    staff = []
    allocations = []

    def __init__(self):
        # populate with model with rooms
        self.populate()
        # populate model with occupants
        self.create_occupants()
        # allocate the rooms to the potential occupants
        self.allocate()

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
        # get the available spaces
        available_offices = self.get_available_offices()
        # first alloate the office spaces
        occ = Occupants.next(staff=self.staff)
        person = None
        for office in available_offices:
            while office.is_not_full() is True:
                try:
                    person = occ.next()
                    office.add_occupant(person)
                except StopIteration:
                    print 'No more staff to allocate'
                    break

            print office
            # update allocations if office has > 1 occupant
            if len(office.occupants) > 0:
                self.allocations.append(office)

    def get_available_offices(self):
        '''
        Returns a list of office rooms with spaces
        '''
        available = []
        for i in self.office_rooms:
            if i.is_not_full():
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
                        space = Room(name=name, usage=usage, capacity=6)
                        self.office_rooms.append(space)
                    else:
                        space = Room(name=name, usage=usage, capacity=4)
                        self.living_rooms.append(space)
