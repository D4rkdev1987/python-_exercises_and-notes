from math import sqrt

sqrt(4)

import sys
sys.path.insert(0, './libs')
from helper import greeting

def render():
    print(greeting('Tiffany', 'Hudgens'))


render()