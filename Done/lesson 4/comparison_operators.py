can_code = False

if can_code == True:
    print('Code')
else:
    print('No')


teacher = 'Dhon'

if teacher.lower() == 'dhon':
    print('Baal')
else:
    print('Valoi')

name = input('Whats your name? ')

if name == 'Saif':
    print('Hey Saif')
    food = 'Pizza'

elif name == 'Maisha':
    print('Love')
    food = 'Burger'

else:
    print('No')
    food = 'Raw'

print(f'You are Eating {food}')

name = input('Whats your name? ')

name = name.lower()

if name != 'saif':
    print('Vaag')
else:
    print('Yes Boss!')
