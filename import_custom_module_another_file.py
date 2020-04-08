# libs/helper.py file
def greeting(first, last):
    return f'Hi {first} {last}!'

# main.py file
import sys
sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('Kristine', 'Hudgens'))


render()