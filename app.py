'''
Usage:
    app.py allocate
    app.py get_allocation
    app.py see_allocations
    app.py see_allocated
    app.py get_unallocated
    app.py see_unallocated
    app.py see_occupants
    app.py see_allocation_analysis
    app.py see_room_occupants <room_name>
    app.py --version
Options:
    -h --help     Show this screen.
    --version     Show version.
'''

from amity import Amity
from docopt import docopt


def init_app():
    '''
    Returns an Amity object populated
    with all rooms
    '''
    return Amity()

if __name__ == '__main__':
    premise = init_app()
    arguments = docopt(__doc__, version='Amity Room Allocator 0.0.1')
    if arguments['allocate']:
        premise.allocate()

    if arguments['get_allocation']:
        premise.get_allocations()

    if arguments['see_allocations']:
        premise.print_allocations()

    if arguments['see_room_occupants']:
        premise.get_room_members(arguments['<room_name>'])

    if arguments['see_allocated']:
        premise.print_allocated()

    if arguments['see_allocation_analysis']:
        premise.print_allocation_analysis()
