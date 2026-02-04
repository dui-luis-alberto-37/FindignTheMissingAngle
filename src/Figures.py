from new_rep import SemiValidateGeom as GeometricFig

Fig1 = GeometricFig()

Fig1.new_line('l1', 'AB')
Fig1.new_line('l2', 'BC')
Fig1.new_line('l3', 'CD')
Fig1.new_line('l4', 'DA')
Fig1.new_line('l5', 'AC')

# print(Fig1.get_triangles())

Fig1.new_angle('ABC', 75)
Fig1.new_angle('ACB', 30)
Fig1.new_angle('CAD', 50)

print(Fig1.is_valid())

Fig2 = GeometricFig()

Fig2.new_line('l1', 'AFGB')
Fig2.new_line('l2', 'BHIC')
Fig2.new_line('l3', 'CJFD')
Fig2.new_line('l4', 'DGHE')
Fig2.new_line('l5', 'EIJA')

Fig2.new_angle('AGE', 100)
Fig2.new_angle('ABC', 58)
Fig2.new_angle('AIB', 93)

print(Fig2.is_valid())


