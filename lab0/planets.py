def find_mars(weight_on_earth):
   return (weight_on_earth * 0.38)

def find_jupiter(weight_on_earth):
   return (weight_on_earth * 2.34)

if __name__ == '__main__':
   weight_on_earth = int(input('What do you weigh on earth? '))

   weight_on_mars = find_mars(weight_on_earth)

   weight_on_jupiter = find_jupiter(weight_on_earth)

   print('\nOn Mars you would weigh', weight_on_mars, 'pounds.',
   '\nOn Jupiter you would weigh', weight_on_jupiter, 'pounds.')

