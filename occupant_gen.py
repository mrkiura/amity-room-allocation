from random import shuffle


class Occupants(object):

    @staticmethod
    def next(staff):
        '''
        Should return the next item on
        the shuffled list staff
        '''
        shuffle(staff)
        if len(staff) > 0:
            for staff_member in staff:
                yield staff_member
