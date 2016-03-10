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
        Calls the methods to randomly allocate
        rooms to people
        '''
        # allocate offices to fellows and staff
        available_offices = self.get_available_rooms('OFFICE')
        self.allocate_rooms(available_offices, self.staff +
                            self.boarding_fellows + self.non_boarding_fellows)

        # allocate rooms to boarding fellows
        available_living_rooms = self.get_available_rooms('LIVING')
        self.allocate_rooms(available_living_rooms, self.boarding_fellows)

    def allocate_rooms(self, rooms, people):
        '''
        Allocates rooms to the list of people
        '''
        next_person = Occupants.next(people)
        person = None
        for room in rooms:
            while room.is_not_full():
                try:
                    person = next_person()
                    room.add_occupant(person)
                except StopIteration:
                    print 'No more staff to allocate'
                    break

            # update allocations if room has > 1 occupant
            if len(room.occupants) > 0:
                self.allocations.append(room)

    def get_available_rooms(self, usage):
        '''
        Returns a list of rooms based on usage
        e.g, returns a list of office spaces
        if usage == 'OFFICE'
        '''
        available = []
        if usage == 'OFFICE':
            for i in self.office_rooms:
                if i.is_not_full():
                    available.append(i)
        else:
            for i in self.living_rooms:
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
