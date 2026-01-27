* repeated segments
	* **v1**: replace it and all its participations (both inside and outside) unless a triangle is completed, and make validation of all new changes before making changes
		* if triangle is completed
			* rather start again
	+ **v2**: replace it and its participations (both)
	+ **v3**: just replace it
	+ **v4**: just replace it

* invalid segments in line
	* **v1**: validation by segment tree
		* if segment not validate don't make changes 
	* **v2**: validation similar algorithm that segment tree
	* **v3-4**: doesn't need
	
+ invalid segments in triangles
	+ **v1-2**: if a triangle has its tree sides try triangle inequality
	+ **v3-4**: doesn't need
	