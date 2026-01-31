# Work Flow
- [x] Recibes a line
- [x] Makes the graph with none values
- [x] Can add values
- [x] Propagates values min max values

## Making the graph
- [x] make leafs
- [x] for each 2 consecutive leafs makes a l-parent and a r-parent
	- [x] Make the associations
- [x] parents become new leafs
- [x] repeat until len(leafs) == 1

## add value
- [x] V2 = segment_trees\[line_key]\[segment] = value
	- [x] is_valid(executes propagation)
- [ ] V1 = segment_trees\[line_key].set_value(name, value, auto_prop = True)
- [x] set_value
	- [x] sets value
	- [x] sets min = value
	- [x] sets max = value

## propagate(name)
- [x] max for the leafs
	- [x] start on root
	- [x] if not value, max = min(max.parents)
	- [x] if value
		- [x] assert value < max.parents, if not is not valid
		- [x] max = value
- [x] min for the parents
	- [x] start on leafs
	- [x] if not value, min = max(min.parents)
	- [x] if value
		- [x] assert value > min
		- [x] min = value

## fixes
- [x] fix AE = 10 and AD = 10 in min propagation