from collections import defaultdict
from itertools import combinations, permutations
from copy import deepcopy



class GeometicRepresentation:
    
    
    def __init__(self, name: str = None):
        #self.name = name
        self.lines_points = defaultdict(list)
        self.points_lines = defaultdict(set)
        
        
        self.points = set()
        #self.lines = set()
        
        self.triangles_names = set()
        
        #self.triangles_config = dict()
        
        self.angles = dict()   
        self.segments = defaultdict(None)     
        
        # self.lasts = {
        #     "line": 0,
        #     # "point": 0,
        # }
        
        self.last_l = 0
        
        self.seg = '_segment'
        self.ang = '_angle'
     
     
     
     
     
     
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
        
        for point in nn_line:
            self.points_lines[point].add(key)
            self.points.add(point)
        
        return None
    
    def add_line(self, nline: list,):      # posible change: triangle generation with each new line
        """Add a line to the geometric representation."""
        
        '''Check if the line is already in the representation. If it is, return None.'''
        for key, line in self.lines_points.items():
            if len(set(nline) & set(line)) >= 2:
                print(f"Line {key} already exists, now expanding.")
                self._expand_line(key, nline)                
                return None

        
        
        # last_l = self.lasts["line"]
        last_l = self.last_l
        
        self.lines_points[f'l{last_l}'] = nline
        
        # self.lasts["line"] += 1
        self.last_l += 1
        
        for point in nline:
            self.points_lines[point].add(f'l{last_l}')
            self.points.add(point)
            
            

    def triangle_internal_sum(self, name):
        """Asserst that the internal angle sum of a triangle is 180 degrees."""
        
        #triangle = self.triangles_config[name]
        #sum_ = 0
        #
        #for point in name:
        #    sum_ += triangle[point+self.ang]
        #
        
        angles = [''.join(angle) for angle in permutations(name, 3)]
        
        sum_ = 0
        for angle in angles:
            sum_ += self.angles[angle]
        
        return sum_ == 180 
        
    
    def get_triagles(self):
        
        """Get the triangles from the geometric representation."""
        
        # new_triangles = set()
        
        lines = self.lines_points.values()
        for line in lines:
            colineal_points = set(line)
            non_colineal = self.points - colineal_points
            for colineal_pair in combinations(colineal_points,2):
                a, b = colineal_pair
                for point in non_colineal:
                    c = point
                    triangle = frozenset([a,b,c])
                    # if triangle not in self.triangles_names:
                    #     new_triangles.add(triangle)
                    self.triangles_names.add(triangle)
                    
        
        # for triangle in new_triangles:
        #     self.triangles_config[triangle] = self._new_triangle(triangle)
        
        
        return self.triangles_names

                        
    def _new_triangle(self, name:set):
        
        
        triangle = {
            'name' : name,
        }
        
        seg = self.seg
        angle = self.ang
        
        segmentes = combinations(name, 2)
        
        for point, segment in zip(name, segmentes):
            
            segment = ''.join(segment)
            triangle[point+angle] = None
            triangle[segment+seg] = None
        
        return triangle
    
    def new_angle(self, name, value):
        
        l, c, r = name
        
        
        lines = self.points_lines
        
        l0_key = (lines[l] & lines[c]).pop()
        l1_key = (lines[c] & lines[r]).pop()
        print(str(l0_key))
        
        
        lines = self.lines_points
        
        l0 = lines[l0_key]
        l1 = lines[l1_key]
        print(lines)
        
        
        l0_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l0):
            if point == l:
                l0_dir = 'l'
            elif point == c:
                c_ubi = i
                break
            
        if l0_dir == 'l':
            L = l0[:c_ubi]
        else:
            L = l0[c_ubi+1:]
            
        
        l1_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l1):
            if point == r:
                l1_dir = 'l'
            elif point == c:
                c_ubi = i
                break
        
        if l1_dir == 'l':
            R = l1[:c_ubi]
        else:
            R = l1[c_ubi+1:]
            
        for l in L:
            for r in R:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
            
            
    def new_segment(self, name, value):
        A, B = name
        points = self.points
        assert (A in points) and (B in points), 'No se encontró el par de puntos'
            
        name = frozenset(name)
        self.segments[name] = value
        line = (self.points_lines[A] & self.points_lines[B]).pop()
    
    def segment_value_consistant(self, line):
        line_points = self.lines_points(line)
        to_check = dict()
        
        for name, value in self.segments.items():
            if len(name & line_points) == 2:
                to_check[name] = value
        
        for AB, BC in combinations(to_check,2):
            
            if (AB & BC):
                