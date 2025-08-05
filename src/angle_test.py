from representations import GeometicRepresentation as Geom
from random import shuffle

angle_value = {
    'DGA':100, 
    'ICA':58,
    'AIC':93,
}

G = Geom()

G.add_line(['C', 'G', 'F', 'A'])

G.add_line(['D', 'I', 'J', 'A'])

G.add_line(['C', 'H', 'I', 'E'])

G.add_line(['D', 'H', 'G', 'B'])

G.add_line(['B', 'F', 'J', 'E'])

angles = list(angle_value.keys())
shuffle(angles)

print(angles)
for angle in angles:
    value = angle_value[angle]
    # print(seg, value)
    G.new_angle(angle, value)
