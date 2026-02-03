from new_rep import GeomSegmentTree as ST

st = ST('ABCDE')

st.set_value('EA', 10)
st.set_value('AD', 9)

print(st.is_valid())
st.print_tree()

