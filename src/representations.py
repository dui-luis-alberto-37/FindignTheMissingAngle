from collections import defaultdict
from itertools import combinations
from copy import deepcopy



class GeometicRepresentation:
    def __init__(self, name: str = None):
        #self.name = name
        self.lines_points = defaultdict(list)
        self.points_lines = defaultdict(list)
        
        
        self.points = set()
        #self.lines = set()
        
        self.triangles = []
        
        
        self.lasts = {
            "line": 0,
            "point": 0,
        }
        
        
        
        
        
        
    def _expand_line(self,key, nline):
        ''' when nline has at least 2 same points with line then this last one expand to coincide
            first by line order, then by nline'''
            
        line = self.lines_points[key]
        
        intersections = set(line) & set(nline)
        n_intersec = len(intersections)
        
        
        
        order_l0 = []
        index_l0 = []
        
        order_l1 = []
        index_l1 = []
        
        
        for i, point in enumerate(line):
            if point in intersections:
                order_l0.append(point)
                index_l0.append(i)
        
        for i, point in enumerate(nline):
            if point in intersections:
                order_l1.append(point)
                index_l1.append(i)
                
        #print(line, nline)
        #print(index_l0, index_l1)
       
        if order_l0 != order_l1:
            '''Se usa si el orden no es el mismo'''
            
            nline = nline[::-1]
            
            index_l1 = [len(nline) - 1 - i for i in index_l1][::-1]
            
            #print(nline)
            #print(index_l1)
         
        last_i, last_j = 0, 0
        
        
        nn_line = []
        for i,j in zip(index_l0, index_l1):
            
            nn_line += line[last_i:i] + nline[last_j:j] + line[i:i+1]
            last_i, last_j = i + 1, j + 1
            #print(nn_line)
            
        nn_line += line[i+1:] + nline[j+1:]
            
        

        self.lines_points[key] = nn_line
                
        
        return None
    
    def add_line(self, nline: list,):
        """Add a line to the geometric representation."""
        
        '''Check if the line is already in the representation. If it is, return None.'''
        for key, line in self.lines_points.items():
            if len(set(nline) & set(line)) >= 2:
                print(f"Line {key} already exists, now expanding.")
                self._expand_line(key, nline)                
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

                        
    def _new_triangle(name):
        triangle = {
            'name' : name,
            'angles' : [None, None, None],
            'longituds' : [None, None, None],
        }
        
        return triangle
            
            
    
        