

class Occupant:

    '''
    A class to model the room occupants-
    fellows and staff
    '''

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.job_type = kwargs['job_type']
        self.room_name = ''
        self.allocated = False

    def __str__(self):
        '''
        Returns a readable string representation
        of the object
        '''
        return ('({0}, {1}, {2})'.format(self.name,
                                         self.job_type, self.room_name))

    def get_job_type(self):
        '''returns staff for a staff or fellow if
        occupant is a fellow
        '''
        return self.job_type
