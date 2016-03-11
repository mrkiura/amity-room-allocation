# amity-room-allocation
An office and living space allocation system. Made in response to checkpoint 1 requirements.

[![Build Status](https://travis-ci.org/andela-akiura/amity-room-allocation.svg?branch=feature-review)](https://travis-ci.org/andela-akiura/amity-room-allocation)
[![Coverage Status](https://coveralls.io/repos/github/andela-akiura/amity-room-allocation/badge.svg?branch=feature-review)](https://coveralls.io/github/andela-akiura/amity-room-allocation?branch=feature-review)

## Installation
Clone the repo 
```
git clone https://github.com/andela-akiura/amity-room-allocation.git
```

Navigate to the root folder
``` 
cd amity-room-allocation 
```

Install the packages
```
pip install -r requirements.txt
```

## Running
Run ``` python app.py allocate ``` to allocate rooms to fellows and staff

Run ``` python app.py see_allocations ``` to view people allocated to a room

Run ``` python app.py --h ``` to get help on usage

## Testing
``` 
nosetests
```

## Credits

[Alex Kiura](https://github.com/andela-akiura)

## License

### The MIT License (MIT)

Copyright (c) 2016 Alex Kiura <alex.kiura@andela.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.

