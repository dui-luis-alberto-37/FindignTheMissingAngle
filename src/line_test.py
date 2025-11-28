from representations import GeometicRepresentation as Geom
from random import shuffle
G = Geom()

# A---3---B---3---C---3---D---3---E

segments_values = {
    'AB': 3,
    'BC': 3,
    'CD': 3,
    'DE': 3,
    'AC': 6,
    'BD': 6,
    'CE': 6,
    'AD': 9,
    'BE': 9,
    'AE': 12
}

segments = list(segments_values.keys())
shuffle(segments)

G.add_line(['A','B','C','D','E'])

# segments = ['AD', 'BD', 'CE', 'AB', 'BC', 'BE', 'DE', 'AE', 'AC', 'CD']
print(segments)
for seg in segments:
    value = segments_values[seg]
    # print(seg, value)
    G.new_segment(seg, value)


for name, value in G.segments.items():
    print(name, value)