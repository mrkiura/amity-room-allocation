'''
Usage:
    app.py allocate
    app.py get_allocation
    app.py see_allocations
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
    premise = Amity()
    arguments = docopt(__doc__, version='Amity Room Allocator 0.0.1')
    if arguments['allocate']:
        premise.allocate()

    if arguments['get_allocation']:
        premise.get_allocations()

    if arguments['see_allocations']:
        premise.print_allocations()
