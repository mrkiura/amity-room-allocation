

class Room:

    '''
    A class to model a single space,
    living or office
    '''

    def __init__(self, **kwargs):
        self.occupants = []
        self.name = kwargs['name']
        self.usage = kwargs['usage']
        self.capacity = kwargs['capacity']

    def __str__(self):
        '''
        Returns a readable string representation
        of the object
        '''
        return ('({0}, {1}, {2})'.format(self.name,
                                         self.capacity, self.occupants))

    def get_occupants(self):
        '''
        Returns a list of people occupying a room
        '''
        return self.occupants

    def add_occupant(self, occupant):
        '''
        Adds a new occupant to the room
        '''
        self.occupants.append(occupant)

    def is_empty(self):
        '''
        Returns True for an empty room
        '''
        return len(self.occupants) == 0

    def is_not_full(self):
        '''
        Returns True for a room with the
        maximum no. of occupants
        '''
        return len(self.occupants) < self.capacity

    def get_room_details(self):
        '''
        Returns name, capacity and the occupants of a room
        '''
        return {'name': self.name,
                'capacity': self.capacity,
                'occupants': self.occupants}

    def get_room_capacity(self):
        '''
        Returns the capacity of the room
        '''
        return self.capacity

    def get_room_usage(self):
        '''
        Returns office for office spaces and living
        for living spaces
        '''
        return self.usage

    def get_vacant_spaces(self):
        '''
        Returns the remaining spaces in a room
        '''
        return self.capacity - len(self.occupants)
