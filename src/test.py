

from representations import GeometicRepresentation as Geom

G = Geom()

G.add_line(['C', 'G', 'F', 'A'])

G.add_line(['D', 'I', 'J', 'A'])

G.add_line(['C', 'H', 'I', 'E'])

G.add_line(['D', 'H', 'G', 'B'])

G.add_line(['B', 'F', 'J', 'E'])


G.new_angle('DGA',100)

G.new_angle('ICA',58)

G.new_angle('AIC',93)

 


print('\n'+'-'*5+'TEST OUTPUT' + '-'*5+'\n')

print(f'lines : points = {G.lines_points}')

print()
print()

print(f'puntos: lineas = {G.points_lines}')

print()
print()

print(f'triangle_names = {G.get_triagles()}')

print()
print()

print(f'all points = {G.points}')

print()
print()

print(f'angles = {G.angles}')
