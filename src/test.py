

from representations import GeometicRepresentation as Geom

G = Geom()

G.add_line(['A', 'B', 'C'])
b = ['D', 'A', 'B', 'E', 'C']
G.add_line(b[::1])


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
