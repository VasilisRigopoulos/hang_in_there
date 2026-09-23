import greetings

print(greetings.hello('bill'))

from greetings import hello

print(hello('bill'))

from greetings import hello as h

print(h('bill'))

import greetings as greet

print(greet.hello('niko'))