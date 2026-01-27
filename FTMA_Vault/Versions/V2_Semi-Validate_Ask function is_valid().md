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
+ add a line
	+ same replace that v3
	+ add line and points
	+ create the segment tree
	+ turn change flag
## get triangles
+ if not flag
	+ return triangle list
+ else
	+ for each pair of points in each line add every non collinear points
## add a segment
+ add it to the line segment tree
## add an angle
## is valid
### segments
### angles

### triangles

