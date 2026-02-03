# is_valid() notes
+ Every call has to check if that estructure is posible.
	+ non  $[l_i\cap l_j]>= 2$  (made in line adding)
	+ non-collinear triangles (made in line adding)
	+ segment adding
		+ triangle consistence.
		+ segment tree consistence
	+ angle adding
		+ triangle consistence
		+ figure consistence??
+ Angles and segments don't know each other (this means no trigonometric functions and no isosceles and equilateral triangle notice this is part of the algorithm)
## extra needs
+ point-lines assignation
+ line change flag (for get_triangles() function)
# Workflow
## add a line
+ [x] same replace that v3
+ [x] add line and points
+ [x] create the segment tree
+ [x] turn change flag
## get triangles
+ [x] if not flag
	+ [x] return triangle list
+ [x] else
	+ [x] for each pair of points in each line add every non collinear points
## add a segment
- [x] just add it to segments
## segment propagation
- [x] identify the lines
+ [x] add it to the line segment tree
+ [x] add it to triangles
	+ [x] find those triangles
## add an angle
- [ ] just add it
## related angles to
- [x] find triangles with the same angle
- [x] find supplementary angles
## propagate angles
- if changes:
	for every angle
## add is_valid function
+ for segments
+ for angles
+ for triangles
## for the future
- [ ] points to lines dic for optimization in locate lines

