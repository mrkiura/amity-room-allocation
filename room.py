

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

    def get_occupants(self, **options):
        '''
        Returns the people occupying a room
        '''
        # if option is number, return the number
        # of people occupying a room
        if options['opt'] == 'number':
            return len(self.occupants)
        return self.occupants

    def add_occupant(self, occupant):
        '''
        Adds a new occupant to the room
        '''
        # only add if there's space
        if not self.is_full():
            self.occupants.append(occupant)
            # return true on successfully allocating
            return True
        else:
            #     # return false on failed allocation
            return False

    def is_full(self):
        '''
        Returns True for a room with the
        maximum no. of occupants
        '''
        return len(self.occupants) >= self.capacity

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
