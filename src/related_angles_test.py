from new_rep import SemiValidateGeom as SVG

Gm = SVG()

Gm.new_line('l1', 'ABCDE')
Gm.new_line('l2', 'GHCIJ')

# Gm.new_angle('ACJ', 100)
print(Gm.related_angles_to('ACJ'))