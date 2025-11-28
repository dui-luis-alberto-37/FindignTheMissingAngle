from new_rep import DummyGeom

Gm = DummyGeom()

Gm.new_line('l1', ['A', 'B', 'C', 'D'])
Gm.new_line('l2', ['C', 'D', 'F', 'G'])
Gm.new_line('l3', ['H', 'I', 'J', 'K'])

Gm.new_angles('ABC', 180)

Gm.new_segment('AB', 52)

print(Gm.points, Gm.lines, Gm.angles, Gm.segments, sep='\n\n')

Gm.new_line('l1', ['A', 'B', 'C', 'D'])