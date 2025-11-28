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
        self.triangles = defaultdict(lambda:{'name': None,
                                            'angles': [None for _ in range(3)],
                                            'segments': [None for _ in range(3)],
                                            'equilatero': False,
                                            'isoseles': False,
                                            'rectangular': False,
                                            'unwrited':True})
        
        #self.triangles_config = dict()
        
        self.angles = dict()   
        self.segments = defaultdict(lambda:None)
        
        # self.lasts = {
        #     "line": 0,
        #     # "point": 0,
        # }
        
        self.last_l = 0
        
        self.seg = '_segment'
        self.ang = '_angle'
        self.changes = False

    def _expand_line(self,key, nline):                      # * delete for simpliest version
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
    
    def add_line(self, nline: list,):                       # ? posible change: triangle generation with each new line
        """Add a line to the geometric representation."""
        
        '''Check if the line is already in the representation. If it is, return None.'''
        for key, line in self.lines_points.items():
            if len(set(nline) & set(line)) >= 2:
                print(f"Line {key} already exists, now expanding.")
                self._expand_line(key, nline)     
                self.changes = True           
                return None
        
        # last_l = self.lasts["line"]
        last_l = self.last_l
        
        self.lines_points[f'l{last_l}'] = nline
        
        # self.lasts["line"] += 1
        self.last_l += 1
        
        for point in nline:
            self.points_lines[point].add(f'l{last_l}')
            self.points.add(point)
        self.changes = True    
    
    def get_triagles(self):                                 # * done for both
        
        """Get the triangles from the geometric representation."""
        
        # new_triangles = set()

        if not self.changes:
            print('No new triangles to add')
            return self.triangles_names
        
        lines = self.lines_points.values()
        for line in lines:
            colineal_points = set(line)
            non_colineal = self.points - colineal_points
            for colineal_pair in combinations(colineal_points,2):
                a, b = colineal_pair
                for point in non_colineal:
                    c = point
                    triangle_name = frozenset([a,b,c])
                    # if triangle not in self.triangles_names:
                    #     new_triangles.add(triangle) #* No need bc is a set
                    
                    self.triangles_names.add(triangle_name)

                    triangle = self.triangles[triangle_name]
                    if triangle['unwrite'] == False:
                        triangle['name'] = list[triangle_name]
                        triangle['unwrite'] == False
        
        # for triangle in new_triangles:
        #     self.triangles_config[triangle] = self._new_triangle(triangle)
        
        self.changes = False
        return self.triangles_names

    # def _new_triangle(self, name:set):                          # * sub function for get_triangles
        # 
        # 
        # triangle = {
            # 'name' : name,
        # }
        # 
        # seg = self.seg
        # angle = self.ang
        # 
        # segmentes = combinations(name, 2)
        # 
        # for point, segment in zip(name, segmentes):
            # 
            # segment = ''.join(segment)
            # triangle[point+angle] = None
            # triangle[segment+seg] = None
        # 
        # return triangle

    def new_angle(self, name, value):                       # ! generative while making seems done
        
        if value >= 180:
            return None
        
        if self.angles[name] == value:
            print('The angle already has that value')
            return None
        l, c, r = name
        
        lines = self.points_lines
        
        l0_key = (lines[l] & lines[c]).pop()
        l1_key = (lines[c] & lines[r]).pop()
        print(str(l0_key))
        
        points = self.lines_points
        
        l0_points = points[l0_key]
        l1_points = points[l1_key]
        print(points)
        
        ''' Detrimines the direction of the line, then spreads '''
        
        l0_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l0_points):
            if point == l:
                l0_dir = 'l'
            elif point == c:
                c_ubi = i
                break
            
        if l0_dir == 'l':
            L = l0_points[:c_ubi]
            L_oposite = l0_points[c_ubi+1:]
        else:
            L = l0_points[c_ubi+1:]
            L_oposite = l0_points[:c_ubi]
        
        l1_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l1_points):
            if point == r:
                l1_dir = 'l'
            elif point == c:
                c_ubi = i
                break
        
        if l1_dir == 'l':
            R = l1_points[:c_ubi]
            R_oposite = l1_points[c_ubi+1:]
        else:
            R = l1_points[c_ubi+1:]
            R_oposite = l1_points[:c_ubi]
        
        # the same angle
        for l in L:
            for r in R:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
                
                self._add_angle_to_triangle(name, value)
        
        # opposite at the vertex: same value
        for l in L_oposite:
            for r in R_oposite:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
                
                self._add_angle_to_triangle(name, value)
        
        # suplenmentary
        for l in L_oposite:
            for r in R:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
                
                self._add_angle_to_triangle(name, (-value)%180)
        
        for l in L:
            for r in R_oposite:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
                
                self._add_angle_to_triangle(name, (-value)%180)
        return True
    
    def _add_angle_to_triangle(self, name, value):              # * sub function for new_angle
        
        set_name = frozenset(name)
        triangle = self.triangles[set_name]
        l, c, r = name
        name = triangle['name']
        index = name.index(c)
        triangle['angles'][index] = value
        return True
    
    def actualize_triagles(self):                           # * done for both
        
        if self.changes:
            
            triangles = self.get_triagles()
        
        else: 
            
            triangles = self.triangles_names
        
        return triangles
    
    def triangle_angle_consistance(self, name):             # done: work for both versions
        """Asserst that the internal angle sum of a triangle is 180 degrees."""
        
        triangle = self.actualize_triagles()
        angles = triangle['angles']
        
        if angles.count(None) >= 2:
            return None
        elif angles.count(None) == 1:
            index = angles.index(None)
            sum_ = angles[(index + 1)%3] + angles[(index + 2)%3]
            value = 180 - sum_
            
            if value <= 0:
                name = triangle['name']
                print(f'Error in the triangle {name}: the angles in {name[(index + 1)%3]} and {name[(index + 2)%3]} sums {sum_}°')
                return False
            
            angles[index] = value
            # sum_ += value
        
        # else:
        
        sum_ = sum(angles)
        assert sum_ == 180, f'Error: the angles sum of {name} is {sum_}, not 180°'
            
        # * usefull for solving algorithm
        if n:=len(set(angles)) < 3:
            triangle['isoseles'] = True
            if n == 1:
                triangle['equilatero'] = True
            
        if 90 in angles:
            triangle['rectangular'] = True
            
        return True
    
    def new_segment(self, name, value):                     # ? lines should contain segment values??? 
        #                                         done: work for both versions
        A, B = name
        points = self.points
        assert (A in points) and (B in points), f'Inconsistencia, No se encontró el par de puntos {set(name)}'
        
        AB = frozenset(name)
        line = (self.points_lines[A] & self.points_lines[B]).pop()
        if self.segment_value_consistance(line, AB, value):
            return True
        
    def segment_value_consistance(self, line, name, value): # todo: needs to be change for v.2

        print(f'Adding {name}')
        if self.segments[name] == value:
            return True
        # print(self.segments)
        
        # * Explanaiton: save all line points and known value segments in the line
        line_points = self.lines_points[line]
        to_check = [name]
        new_segments = {
            name: value
        }
        
        for name in self.segments:
            # name = set(name)
            if self.segments[name]:
                if len(name & set(line_points)) == 2:
                    to_check.append(name)
        # print(to_check)
        
        # * to validate new segments genertated
        
        # * These cases considered for each pair of known segments
        # *     Case 1: Consecutive segments
        # *     Case 2: Overlaped segments
        # *     Case 3: Non consecutive segments
        # ?     Case 4? One inside the other
        
        consistant_pair_check = list(combinations(to_check,2)) # kinda queue
        print(f'pairs : {consistant_pair_check}')

        for AB, CD in consistant_pair_check:
            new_to_check = 'No new changes'
            print(f'analizing {AB, CD}')
            if AB in new_segments:
                AB_value = new_segments[AB]
            else:
                AB_value = self.segments[AB]
            if CD in new_segments:
                CD_value = new_segments[CD]
            else:
                CD_value = self.segments[CD]
            
            sum_ = AB_value + CD_value
            diff = abs(AB_value - CD_value)
            
            
            
            
            find_order = []
            
            union = AB | CD
            intersect = AB & CD
            
            long_segment = set()
            
            for point in line_points:    
                
                if point in union:
                    find_order.append(point)
                
            long_segment.add(find_order[0])
            long_segment.add(find_order[-1])
            
            
            if intersect: # * CASE 1
                
                sym_diff = AB ^ CD
                
                # * Case 1.1 AB, BC
                if sym_diff == long_segment:
                    print('CASE 1.1')
                    
                    BC = CD
                    AC = sym_diff
                    
                    if AC_value := self.segments[AC]:
                        assert AC_value == sum_, f'Inconsistencia: los segmentos {AB} + {BC} != {AC}'
                    elif AC in new_segments:
                        assert new_segments[AC] == sum_, f'Inconsistencia: los segmentos {AB} + {BC} != {AC}'
                    else:
                        #self.segments[AC] = sum_
                        new_to_check = [(AC, seg) for seg in to_check]
                        consistant_pair_check += new_to_check
                        to_check.append(AC)
                        new_segments[AC] = sum_
                
                
                # * Case 1.2 AB, AC
                else:
                    print('CASE 1.2')
                    BC = sym_diff
                    
                    if BC_value := self.segments[BC]:
                        assert BC_value == diff, f'Inconsistencia: los segmentos |{AB} - {CD}| != {BC}'
                    elif BC in new_segments:
                        assert new_segments[BC] == diff, f'Inconsistencia: los segmentos {AB} + {BC} != {AC}'
                    else:
                        new_to_check = [(BC, seg) for seg in to_check]
                        consistant_pair_check += new_to_check
                        to_check.append(BC)
                        new_segments[BC] = diff
                        
            
            else: # * No intersection means case 2 or 3
                # print('h')
                
                if long_value := self.segments[frozenset(long_segment)]: 
                    
                    # * Case 2 or 3 decision
                    if ((first_2 := set(find_order[:2])) == AB) or (first_2 == CD):
                        overlap = False
                    else:
                        overlap = True
                    
                    middle_segment = frozenset(find_order[1:3])
                    middle_value = self.segments[middle_segment]
                    if middle_segment in new_segments:
                        middle_value = new_segments[middle_segment]
                    
                    
                    if overlap: # * CASE 2
                        print('CASE 2')

                        assert long_value < sum_, f'Inconsistencia: la suma de los segmentos {AB} + {CD} <= {long_segment}'
                        if middle_value:
                            assert middle_value == sum_ - long_value, f'Inconsistencia: la suma de los segmentos {AB} + {CD} - {long_segment} != {middle_segment}'
                        else:
                            new_to_check = [(middle_segment, seg) for seg in to_check]
                            consistant_pair_check += new_to_check
                            to_check.append(middle_segment)
                            new_segments[middle_segment] = sum_ - long_value
                            
                    
                    else: # * CASE 3
                        
                        print('CASE 3')
                        assert long_value > sum_, f'Inconsistencia: la suma de los segmentos {AB} + {CD} >= {long_segment}'
                        if middle_value:
                            assert middle_value == long_value - sum_,  f'Inconsistencia: la suma de los segmentos  {long_segment} - ({AB} + {CD}) != {middle_segment}'
                        else:
                            new_to_check = [(middle_segment, seg) for seg in to_check]
                            consistant_pair_check += new_to_check
                            to_check.append(middle_segment)
                            new_segments[middle_segment] = long_value - sum_
            
            print(new_to_check)
        
        
        # * if no inconsistantce
        for name, value in new_segments.items():
            self.segments[name] = value
            self._add_segment_to_triangles(name, value)
        return True

    def _add_segment_to_triangles(self, seg, value):        # done: work for both versions
        
        A, B = seg
        line = self.points_lines[A] & self.points_lines[B]

        colineal_points = self.lines_points[line]
        non_conlineal_p = self.points - set(colineal_points)

        for C in non_conlineal_p:
            name = frozenset([A,B,C])
            triangle = self.triangles[name]
            name = triangle['name']
            index = name.index(C)
            triangle['segments'][index] = value


class GeometicRepresentation_v2: # this version doesn't generates predicted values, just checks for no geometrical errors
    
    def __init__(self, name: str = None):
        #self.name = name
        self.lines_points = defaultdict(list)
        self.points_lines = defaultdict(set)
        
        
        self.points = set()
        #self.lines = set()
        
        self.triangles_names = set()
        self.triangles = defaultdict(lambda:{'name': None,
                                            'angles': [None for _ in range(3)],
                                            'segments': [None for _ in range(3)],
                                            'equilatero': False,
                                            'isoseles': False,
                                            'rectangular': False,
                                            'unwrited':True})
        
        #self.triangles_config = dict()
        
        self.angles = dict()   
        self.segments = defaultdict(lambda:None)
        
        # self.lasts = {
        #     "line": 0,
        #     # "point": 0,
        # }
        
        self.last_l = 0
        
        self.seg = '_segment'
        self.ang = '_angle'
        self.changes = False
        
        self.line_value_changed = set()
        self.line_point_changed = set()
    
    def _replece_line(self, key, line, nline):              # * done:
        l1 = set(line)
        l2 = set(nline)
        
        to_delete_points = l1 - l2
        for point in to_delete_points:
            self.points_lines[point].remove(key)
            if not self.points_lines[point]:
                del self.points_lines[key]
                self.points.remove(point)
        
        self.changes = True
        self.lines_points[key] = nline
        self.line_point_changed.add(key)
        print(f'The line {key}:{line} was replaced with {nline}')
        return True
    
    def add_line(self, nline: list,):                       # * done:
        '''Add a line to the geometric representation.'''
        
        '''Check if the line is already in the representation. If it is, return None.'''
        
        for key, line in self.lines_points.items():
            if len(set(nline) & set(line)) >= 2:
                print(f"Line {key} already exists: {line}")
                print('Want to replace')
                res = input('Y/n')
                if res == 'Y' or not res:
                    return self._replece_line(key, line, nline)
                else:
                    return None
        
        # last_l = self.lasts["line"]
        last_l = self.last_l
        key = f'l{last_l}'
        self.lines_points[key] = nline
        
        # self.lasts["line"] += 1
        self.last_l += 1
        
        for point in nline:
            self.points_lines[point].add(f'l{last_l}')
            self.points.add(point)
        self.changes = True
        self.line_point_changed.add(key)
        return True
    
    def get_triagles(self):                                 # * done:
        
        """Get the triangles from the geometric representation."""
        
        # new_triangles = set()

        if not self.changes:
            print('No new triangles to add')
            return self.triangles_names
        
        lines = self.lines_points.values()
        for line in lines:
            colineal_points = set(line)
            non_colineal = self.points - colineal_points
            for colineal_pair in combinations(colineal_points,2):
                a, b = colineal_pair
                for point in non_colineal:
                    c = point
                    triangle_name = frozenset([a,b,c])
                    # if triangle not in self.triangles_names:
                    #     new_triangles.add(triangle) #* No need bc is a set
                    
                    self.triangles_names.add(triangle_name)

                    triangle = self.triangles[triangle_name]
                    if triangle['unwrite'] == False:
                        triangle['name'] = list[triangle_name]
                        triangle['unwrite'] == False
        
        # for triangle in new_triangles:
        #     self.triangles_config[triangle] = self._new_triangle(triangle)
        
        self.changes = False
        return self.triangles_names

    def new_angle(self, name, value):                       # * done:
        
        if value >= 180:
            print('Ingrese solo angulos menores de 180°')
            return None
        
        if self.angles[name] == value:
            print('The angle already has that value')
            return None
        l, c, r = name
        
        lines = self.points_lines
        
        l0_key = (lines[l] & lines[c]).pop()
        l1_key = (lines[c] & lines[r]).pop()
        print(str(l0_key))
        
        points = self.lines_points
        
        l0_points = points[l0_key]
        l1_points = points[l1_key]
        print(points)
        
        ''' Detrimines the direction of the line, then spreads '''
        
        l0_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l0_points):
            if point == l:
                l0_dir = 'l'
            elif point == c:
                c_ubi = i
                break
            
        if l0_dir == 'l':
            L = l0_points[:c_ubi]
            L_oposite = l0_points[c_ubi+1:]
        else:
            L = l0_points[c_ubi+1:]
            L_oposite = l0_points[:c_ubi]
        
        l1_dir = 'r'
        c_ubi = None
        for i, point in enumerate(l1_points):
            if point == r:
                l1_dir = 'l'
            elif point == c:
                c_ubi = i
                break
        
        if l1_dir == 'l':
            R = l1_points[:c_ubi]
            R_oposite = l1_points[c_ubi+1:]
        else:
            R = l1_points[c_ubi+1:]
            R_oposite = l1_points[:c_ubi]
        
        # the same angle
        for l in L:
            for r in R:
                name = l+c+r
                
                #self.angle[name][c+self.ang] = value
                self.angles[name] = value
                
                self._add_angle_to_triangle(name, value)
        
        return True
    
    def _add_angle_to_triangle(self, name, value):              # * sub function for new_angle
        
        set_name = frozenset(name)
        triangle = self.triangles[set_name]
        l, c, r = name
        name = triangle['name']
        index = name.index(c)
        triangle['angles'][index] = value
        return True
    
    def actualize_triagles(self):                           # * done
        
        if self.changes:
            
            triangles = self.get_triagles()
        
        else: 
            
            triangles = self.triangles_names
        
        return triangles
    
    def triangle_angle_consistance(self, name):             # done: work for both versions
        """Asserst that the internal angle sum of a triangle is 180 degrees."""
        
        triangle = self.actualize_triagles()
        angles = triangle['angles']
        
        if angles.count(None) >= 2:
            return None
        elif angles.count(None) == 1:
            index = angles.index(None)
            sum_ = angles[(index + 1)%3] + angles[(index + 2)%3]
            value = 180 - sum_
            
            if value <= 0:
                name = triangle['name']
                print(f'Error in the triangle {name}: the angles in {name[(index + 1)%3]} and {name[(index + 2)%3]} sums {sum_}°')
                return False
            
            angles[index] = value
            # sum_ += value
        
        # else:
        
        sum_ = sum(angles)
        assert sum_ == 180, f'Error: the angles sum of {name} is {sum_}, not 180°'
            
        # * usefull for solving algorithm
        if n:=len(set(angles)) < 3:
            triangle['isoseles'] = True
            if n == 1:
                triangle['equilatero'] = True
            
        if 90 in angles:
            triangle['rectangular'] = True
            
        return True
    
    def new_segment(self, name, value):
        self.segments[frozenset(name)] = value
        
        
    def segment_value_consistance(self, line, name, value): # todo: needs to be change for v.2

        print(f'Adding {name}')
        if self.segments[name] == value:
            return True
        # print(self.segments)
        
        # * Explanaiton: save all line points and known value segments in the line
        line_points = self.lines_points[line]
        to_check = [name]
        new_segments = {
            name: value
        }
        
        ading = 0
        inside_points = []
        for point in line_points:
            if point in name:
                ading = (ading+1)%2
            if ading:
                inside_points.append(point)
        
        
        
        # * to validate new segments genertated
        
        
        
        # * if no inconsistantce
        for name, value in new_segments.items():
            self.segments[name] = value
            self._add_segment_to_triangles(name, value)
        return True
    
        # * workflow for line (no recursive)
        # * all size one are considered consistence,
        consisted_seg_values = {}
        for i in range(len(line_points)):
            one_name = frozenset([line_points[i], line_points[i+1]])
            consisted_seg_values[one_name] = self.segment_value_consistance
        # * we exend the size one in all but last and check inside till we got the line
        # * we just check the halves, since the insides are checked it should work
        # * each we belive is done we add it to a global dic
        

    def _add_segment_to_triangles(self, seg, value):        # done: work for both versions
        
        A, B = seg
        line = self.points_lines[A] & self.points_lines[B]

        colineal_points = self.lines_points[line]
        non_conlineal_p = self.points - set(colineal_points)

        for C in non_conlineal_p:
            name = frozenset([A,B,C])
            triangle = self.triangles[name]
            name = triangle['name']
            index = name.index(C)
            triangle['segments'][index] = value
