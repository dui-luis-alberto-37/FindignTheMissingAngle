from collections import defaultdict
from itertools import combinations



class GeometicRepresentation:
    def __init__(self, name: str = None):
        #self.name = name
        self.lines_points = defaultdict(list)
        self.points_lines = defaultdict(list)
        
        
        self.points = set()
        #self.lines = set()
        #self.triangles = set()
        
        
        self.lasts = {
            "line": 0,
            "point": 0,
        }
        
        
        
    def expand_line(self,key, nline):
        ''' when nline has at least 2 same points with line then this lastone expand to coincide
            respetin line order'''
            
        line = self.lines_points[key]
        
        intersections = set(line) & set(nline)
        n_intersec = len(intersections)
        
        # inverse_order = False
        
        j = 0
        nn_line = []
        
        while line:
            p0 = line.pop(0)
            nn_line.append(p0)
            if p0 in intersections:
                left  = []
                right = []
                for p1 in nline:
                    if p1 in intersections and p1 != p0:
                        inverse_order = True
        
        
        return None
    
    def add_line(self, nline: list,):
        """Add a line to the geometric representation."""
        
        '''Check if the line is already in the representation. If it is, return None.'''
        for key, line in self.lines_points.items():
            if len(set(nline) & set(line)) >= 2:
                print(f"Line {key} already exists.")
                self.expand_line(key, nline)                
                return None

        
        
        last_l = self.lasts["line"]
        self.lines_points[f'l{last_l}'] = nline
        
        self.lasts["line"] += 1
        
        for point in nline:
            self.points_lines[point].append(f'l{last_l}')
            self.points.add(point)
            
            

    def triangle_internal_sum(triangle):
        """Asserst that the internal angle sum of a triangle is 180 degrees."""
        x, y, z = triangle
        return x + y + z == 180  
        
    
    def get_triagles(self):
        """Get the triangles from the geometric representation."""
        triangles = set()
        lines = self.lines_points.values()
        for line in lines:
            colineal_points = set(line)
            non_colineal = self.points - colineal_points
            for colineal_pair in combinations(colineal_points,2):
                a, b = colineal_pair
                for point in non_colineal:
                    c = point
                    triangles.add(set([a,b,c]))
        

                        

            
            
            
        return triangles
        