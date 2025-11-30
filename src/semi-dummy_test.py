from new_rep import SemiDummyTriangle, SemiDummyGeom

triangle = SemiDummyTriangle('ABC')
triangle.angles['A'] = 0
triangle.angles['B'] = 25
triangle.angles['C'] = 3456

print(triangle.vertices, triangle.segments, triangle.angles, sep='\n\n')

Gm = SemiDummyGeom()

Gm.new_line('l1', 'ABCD')

Gm.new_segment('AB', 10)

Gm.new_angles('ABC', 20)
print(Gm.lines, Gm.triangles)

for triangle in Gm.triangles.values():
   print(triangle.segments, triangle.angles, sep='\n\n')
