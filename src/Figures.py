from new_rep import SemiValidateGeom as GeometricFigV2, SemiDummyGeom as GeometricFigV3, DummyGeom as GeometricFigV4

Fig1_V2 = GeometricFigV2()

Fig1_V2.new_line('l1', 'AB')
Fig1_V2.new_line('l2', 'BC')
Fig1_V2.new_line('l3', 'CD')
Fig1_V2.new_line('l4', 'DA')
Fig1_V2.new_line('l5', 'AC')

Fig1_V2.new_angle('ABC', 75)
Fig1_V2.new_angle('ACB', 30)
Fig1_V2.new_angle('CAD', 50)

print(Fig1_V2.is_valid())

Fig2_V2 = GeometricFigV2()

Fig2_V2.new_line('l1', 'AFGB')
Fig2_V2.new_line('l2', 'BHIC')
Fig2_V2.new_line('l3', 'CJFD')
Fig2_V2.new_line('l4', 'DGHE')
Fig2_V2.new_line('l5', 'EIJA')

Fig2_V2.new_angle('AGE', 100)
Fig2_V2.new_angle('ABC', 58)
Fig2_V2.new_angle('AIB', 93)

print(Fig2_V2.is_valid())

'''-------------------------------------------------------------------------'''

Fig1_V3 = GeometricFigV3()

Fig1_V3.new_line('l1', 'AB')
Fig1_V3.new_line('l2', 'BC')
Fig1_V3.new_line('l3', 'CD')
Fig1_V3.new_line('l4', 'DA')
Fig1_V3.new_line('l5', 'AC')

Fig1_V3.new_angle('ABC', 75)
Fig1_V3.new_angle('ACB', 30)
Fig1_V3.new_angle('CAD', 50)


Fig2_V3 = GeometricFigV3()

Fig2_V3.new_line('l1', 'AFGB')
Fig2_V3.new_line('l2', 'BHIC')
Fig2_V3.new_line('l3', 'CJFD')
Fig2_V3.new_line('l4', 'DGHE')
Fig2_V3.new_line('l5', 'EIJA')

Fig2_V3.new_angle('AGE', 100)
Fig2_V3.new_angle('ABC', 58)
Fig2_V3.new_angle('AIB', 93)

'''--------------------------------------------------------------------'''

Fig1_V4 = GeometricFigV4()

Fig1_V4.new_line('l1', 'AB')
Fig1_V4.new_line('l2', 'BC')
Fig1_V4.new_line('l3', 'CD')
Fig1_V4.new_line('l4', 'DA')
Fig1_V4.new_line('l5', 'AC')

Fig1_V4.new_angle('ABC', 75)
Fig1_V4.new_angle('ACB', 30)
Fig1_V4.new_angle('CAD', 50)


Fig2_V4 = GeometricFigV4()

Fig2_V4.new_line('l1', 'AFGB')
Fig2_V4.new_line('l2', 'BHIC')
Fig2_V4.new_line('l3', 'CJFD')
Fig2_V4.new_line('l4', 'DGHE')
Fig2_V4.new_line('l5', 'EIJA')

Fig2_V4.new_angle('AGE', 100)
Fig2_V4.new_angle('ABC', 58)
Fig2_V4.new_angle('AIB', 93)