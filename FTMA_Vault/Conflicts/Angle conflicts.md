## Assertions
+ len == 3
+ only positives
+ no grater than 180
+ existing points
---

* **repeated angles** (same angle, diff value)
	*  **v1**: 
		if triangle **not completed**:
		* replace it and all its participations unless a triangle is completed, and make validation of all new changes before making changes
	* if triangle is completed 
		+ rather start again, than cascade effect 
	* **v2**: replace it and its participations
	* **v3-4**: replace it (just it and no propagation)
* **illogical values** (>= 180 or <= 0)
	* reject it in all
* **len == 3**
+ **intern value inconsistency**:
	+ v1:
--- --- --- 
* invalid angles and inconsistency in angles
	* **v1**:
		* if it completes a triangle:
			can't be change, better start again or delete all insides
		* elif it makes sums grater than 180:
			negated and ask to change it
	+ **v2**: compile all wrongs and print them by triangles
	+ **v3**: send a error message of the wrong triangle
	+ **v4**: print(no negatives or angles > 180 allowed)
	