from __future__ import print_function
from room import Room
from occupant import Occupant
from occupant_gen import Occupants


class Amity(object):

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
        self.allocations = []
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
        # allocate office rooms
        self.allocate_rooms(
            self.office_rooms, self.boarding_fellows +
            self.non_boarding_fellows + self.staff)

        # allcoate living rooms
        self.allocate_rooms(self.living_rooms, self.boarding_fellows)

    def allocate_rooms(self, rooms, people):
        '''
        Allocates rooms to the list of people
        '''
        next_person = Occupants.next(people)
        has_staff = True
        for room in rooms:
            if has_staff:
                # if has_staff:
                while room.is_not_full():
                    try:
                        person = next_person.next()
                        room.add_occupant(person)
                    except StopIteration:
                        has_staff = False
                        break
                if len(room.occupants) > 0:
                    self.allocations.append(room)
            else:
                break

    def get_available_rooms(self, usage):
        '''
        Returns a list of rooms based on usage
        e.g, returns a list of office spaces
        if usage == 'OFFICE'
        '''
        available = []
        if usage == 'OFFICE':
            for i in [room for room in
                      self.office_rooms if room.is_not_full()]:
                    available.append(i)
        else:
            for i in [room for room in
                      self.living_rooms if room.is_not_full()]:
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
                        usage = 'OFFICE'
                        space = Room(name=name, usage=usage, capacity=6)
                        self.office_rooms.append(space)
                    else:
                        usage = 'LIVING'
                        space = Room(name=name, usage=usage, capacity=4)
                        self.living_rooms.append(space)

    def print_allocations(self):
        '''
        Prints a room and the occupants in that room
        '''
        for room in self.allocations:
            print('{0} ({1})'.format(room.name, room.usage))
            for person in room.occupants:
                print(person.name, end=', ')
            print('\n')

    def print_allocated(self):
        '''
        Prints a list of employees who have been
        allocated roooms
        '''
        allocated_people = self.get_allocated_occupants()
        for person in allocated_people:
            print(person)

    def get_allocated_occupants(self):
        allocated = []
        for room in self.allocations:
            for occupant in room.occupants:
                allocated.append((occupant.name, room.name))
        return allocated

    def analyze_allocations(self):
        '''
        Returns the number of rooms available,
        number of total personnel, number of allocated vs
        number of unallocated
        '''
        total_number_of_rooms = len(self.living_rooms + self.office_rooms)
        number_of_allocated_rooms = len(self.allocations)
        number_of_unallocated_rooms = total_number_of_rooms - \
            number_of_allocated_rooms
        number_of_total_occupants = len(self.staff +
                                        self.non_boarding_fellows +
                                        self.boarding_fellows)
        number_of_allocated_occupants = len(self.get_allocated_occupants())
        number_of_unaallocated_occupants = len(
            self.get_unallocated_occupants())
        return {'total rooms': total_number_of_rooms,
                'allocated rooms': number_of_allocated_rooms,
                'unallocated rooms': number_of_unallocated_rooms,
                'total occupants': number_of_total_occupants,
                'allocated occupants': number_of_allocated_occupants,
                'unallocated occupants': number_of_unaallocated_occupants
                }

    def print_allocation_analysis(self):
        print(self.analyze_allocations())

    def print_unallocated(self):
        '''
        Prints a list of people
        not allocated to any rooms
        '''
        pass
        unallocated_people = self.get_unallocated()
        for unallocated_person in unallocated_people:
            print(unallocated_person)

    def get_unallocated_occupants(self):
        '''
        Returns a list of occupants who
        are not allocated to any rooms
        '''
        allocated = []
        for room in self.allocations:
            allocated += room.occupants
        return list(set(
            self.staff + self.boarding_fellows +
            self.non_boarding_fellows) - set(allocated))

    def get_room_members(self, room_name):
        '''
        Print list of room members
        '''
        for room in self.allocations:
            if room.name == room_name:
                print(room.name, '\n')
                for i in room.occupants:
                    print(i)
