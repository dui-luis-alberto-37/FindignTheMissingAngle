

from representations import GeometicRepresentation as Geom

G = Geom()

G.add_line(['A', 'B', 'C'])
b = ['D', 'A', 'B', 'E', 'C']
G.add_line(b[::1])


print('\n'+'-'*5+'TEST OUTPUT' + '-'*5+'\n')

print(G.lines_points)
print(G.get_triagles())