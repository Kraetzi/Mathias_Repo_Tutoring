import os

"""
You can find the list of function of os.path at
https://docs.python.org/3/library/os.path.html
"""

print('---- __file__')
print(f'{__file__}\n')

print('---- dirname()')
print(f'{os.path.dirname(__file__)}\n')

print('---- exists')
print(f'Does __file__ exists? {os.path.exists(__file__)}\n')

working_directory = os.path.dirname(__file__)
file_path = os.path.join(working_directory, 'sample.txt')
print('----- join')
print(f'{file_path}\n')

# Sometimes you will see people using directly the join and dirname in the same line
# file_path = os.path.join(os.path.dirname(__file__), 'sample.txt')
#
# You can see even worse things like...
#
# with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as file:
#   pass

print('----- opening file')
with open(file_path) as file:
    print(file.read())
