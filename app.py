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
    # print(arguments)
    if arguments['allocate']:
        premise.allocate()

    if arguments['get_allocation']:
        premise.get_allocations()

    if arguments['see_allocations']:
        premise.print_allocations()

# """Naval Fate.
# Usage:
#   naval_fate.py ship new <name>...
#   naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
#   naval_fate.py ship shoot <x> <y>
#   naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
#   naval_fate.py -h | --help
#   naval_fate.py --version
# Options:
#   -h --help     Show this screen.
#   --version     Show version.
#   --speed=<kn>  Speed in knots [default: 10].
#   --moored      Moored (anchored) mine.
#   --drifting    Drifting mine.
# """
# from docopt import docopt


# if __name__ == '__main__':
#     arguments = docopt(__doc__, version='Naval Fate 2.0')
#     print(arguments)