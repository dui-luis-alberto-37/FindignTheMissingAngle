# is_valid() notes
+ Every call has to check if that structure is possible.
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
- [x] just add it
## related angles to
- [x] find triangles with the same angle
- [x] find supplementary angles
## propagate angles
- if changes:
	- [x] for every angle
		- [x]  if it has a value assert is the same as which has to be add it
		- [x]  if not just add it
## add is_valid function
+ [ ] for segments
	+ [x] no problem with segment tree
	+ [ ] no problem with triangle inequality
+ [ ] for angles
	+ [ ] for each triangle
		+ [ ] depending of how many values 
			+ [ ] assert sum never grater than 180
## for the future
- [ ] points to lines dic for optimization in locate lines
- [ ] better value propagation for segments
