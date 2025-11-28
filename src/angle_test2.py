from representations import GeometicRepresentation as Geo

G = Geo()

G.add_line(['A','B'])
G.add_line(['A','C'])

G.new_angle('ABC',45)

print(G.angles)