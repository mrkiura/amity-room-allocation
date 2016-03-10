class Occupants(object):

    @staticmethod
    def next(staff):
        '''
        Should return the next item on
        the list ls
        '''
        if len(staff) > 0:
            for staff_member in staff:
                yield staff_member
