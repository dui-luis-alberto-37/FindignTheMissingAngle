
Replace line is better than expand it

## Conflicts an solutions

* repeated lines 
	* **v1-2**: replace it and all its participations
	* **v3-4**: replace it (just it an no propagation)
	
* repeated angles (same angle, diff value)
	*  **v1**: replace it and all its participations unless a triangle is completed, and make validation of all new changes before making changes
		* if triangle is completed 
			+ rather start again, than cascade effect 
	* **v2**: replace it and its participations
	* **v3-4**: replace it (just it and no propagation)
	
* repeated segments
	* **v1**: replace it and all its participations (both inside and outside) unless a triangle is completed, and make validation of all new changes before making changes
		* if triangle is completed
			* rather start again
	+ **v2**: replace it and its participations (both)
	+ **v3**: just replace it
	+ **v4**: just replace it
	
* invalid angles and inconsistence in angles
	* **v1**:
		* if it completes a triangle:
			can't be change, better start again or delete all insides
		* elif it makes sums grater than 180:
			negated and ask to change it
	+ **v2**: compile all wrongs and print them by triangles
	+ **v3**: send a error message of the wrong triangle
	+ **v4**: print(no negatives or angles > 180 allowed)
	
* invalid segments in line
	* **v1**: validation by segment tree
		* if segment not validate don't make changes 
	* **v2**: validation similar algorithm that segment tree
	* **v3-4**: doesn't need
	
+ invalid segments in triangles
	+ **v1-2**: if a triangle has its tree sides try triangle inequality
	+ **v3-4**: doesn't need
	
* new triangles
	* **v1**:  new each line
		* advantages:
			* no need of manual update
		* disadvantages:
			* difficult to remove triangles when replace
	* **v2**: get triangles()
	* **v3**: just add it with ¿¿segments?? and angles
	* **v4**: no need
	
+ impossible figure
	+ cant be made without trigonometric functions

#solutions 
#coficts
