import math
from itertools import combinations
from copy import deepcopy

class DummyGeom:
   def __init__(self):
      self.lines = dict()
      self.points = set()
      self.angles = dict()
      self.segments = dict()
   
   def new_line(self, key:str, points:list):
      self.lines[key] = points
      for point in points:
         self.points.add(point)
   
   def new_angles(self, name:str, value):
      if len(name) != 3:
         raise ValueError("El nombre tiene que tener 3 caracteres que sirvan de puntos.")
      if value <= 0:
         raise ValueError("Los angulos deben ser positivos.")
      if value >= 180:
         raise ValueError("Los angulos deben ser menores a 180.")
      else:
         self.angles[name] = value
   
   def new_segment(self, name:str, value):
      if value <= 0:
         raise ValueError("Los lados deben ser positivos.")
      name = frozenset(name)
      self.segments[name] = value

class SemiDummyTriangle:
   def __init__(self, name):
      assert len(name) == 3, 'La cardinalidad de la variable [name] debe ser 3 elementos como sus vertices'
      self.name = frozenset(name)
      
      self.vertices = list(name)
      
      self.angles = {
         angle : None for angle in name
      } 
      self.segments = {
         self.name - set(seg) : None for seg in name
      }
   
class SemiDummyGeom:
   def __init__(self):
      print('''Antes de agregar valores de segmentos y angulos asegurate de colocar 
            todos los puntos y lineas''')
      self.lines = dict()
      self.points = set()
      self.angles = dict()
      self.segments = dict()
      self.triangles = dict()
   
   def new_line(self, key:str, points:list):
      points = list(points)
      for k, line in self.lines:
         intersec = set(line) & set(points)
         if len(intersec) >= 2:
            del self.lines[k]
            self.points = self.points - set(line)
            print(f'La linea {k}:{line} será remplazada por la linea {key}:{points} debido a que comparten los siguientes puntos {intersec}')
            break
      
      self.lines[key] = points
      self.points = self.points | set(points)
         
   def new_segment(self, name:str, value):
      if value <= 0:
         raise ValueError("Los lados deben ser positivos.")
      name = frozenset(name)
      self.segments[name] = value
      
      triangles_with_seg = [frozenset(name ^ set(point)) for point in self.points-set(name)]
      for triangle in triangles_with_seg:
         self.triangles[triangle] = SemiDummyTriangle(triangle)
         self.triangles[triangle].segments[name] = value
   
   def new_angle(self, name:str, value):
      if len(name) != 3:
         raise ValueError("El nombre tiene que tener 3 caracteres que sirvan de puntos.")
      if value <= 0:
         raise ValueError("Los angulos deben ser positivos.")
      if value >= 180:
         raise ValueError("Los angulos deben ser menores a 180.")
      if set(name) & self.points != set(name):
         raise ValueError("Los puntos deven ser puntos existentes")
      else:
         self.angles[name] = value
         triangle_name = frozenset(name)
         self.triangles[triangle_name].angles[name[1]] = value
   
class Node:
   def __init__(self, name, max_ = math.inf, min_ = 0, value = None, rparent = None, lparent = None):
      self.name = name
      self.max = max_
      self.min = min_
      if value:
         assert value > 0, 'El valor debe ser mayor a 0'
      self.value = value
      self.left = None
      self.right = None
      self.rparent = rparent
      self.lparent = lparent
   
class GeomSegmentTree:
   def __init__(self, line):
      self.line = line
      self.segments = dict()
      self._getsegments()
      
      self.root = self.line[0] + self.line[-1]
      self.leafs = [line[i:i+2] for i in range(len(line)-1)]
   
   def print_tree(self):
      parents = [self.root]
      while parents:
         print(parents)
         leafs = set()
         for parent in parents:
            parent = frozenset(parent)
            print(self.segments[parent].name,':', self.segments[parent].min, '-', self.segments[parent].value,'-', self.segments[parent].max, sep='\t')
            
            left = self.segments[parent].left
            right = self.segments[parent].right
            if left:
               leafs.add(left)
            if right:
               leafs.add(right)
         print()
         parents = leafs
   
   def _getsegments(self):
      line = self.line
      
      leafs = [line[i:i+2] for i in range(len(line)-1)]
      for v in leafs:
         self.segments[frozenset(v)] = Node(v)
      
      while len(leafs) > 1:
         # print(leafs)
         leafs = [self.parent(leafs[i], leafs[i+1]) for i in range(len(leafs)-1)]
      # print(leafs)
   
   def parent(self, l, r):
      p_name = l[0] + r[-1]
      p = self.segments[frozenset(p_name)] = Node(p_name)
      p.left = frozenset(l)
      p.right = frozenset(r)
      self.segments[frozenset(l)].rparent = frozenset(p_name)
      self.segments[frozenset(r)].lparent = frozenset(p_name)
      return p_name
   
   def set_value(self, name, value, auto_prop = False):
      v = self.segments[frozenset(name)]
      v.value = value
      v.max = value
      v.min = value
      
      if auto_prop:
         self.min_propagation(name)
         self.max_propagation(name)
   
   def max_propagation(self, from_ = None):
      # print('max from:',from_)
      if from_:
         parents = [from_]
      else:
         parents = [self.root]
      leafs = set()
      for parent in parents:
         leafs.add(self.segments[frozenset(parent)].left)
         leafs.add(self.segments[frozenset(parent)].right)
      
      while leafs:
         # print(leafs)
         new_leafs = set()
         for leaf in leafs:
            v = self.segments[leaf]
            if v.lparent:
               lp = self.segments[v.lparent]
            else:
               lp = Node('__')
            if v.rparent:
               rp = self.segments[v.rparent]
            else:
               rp = Node('__')
            max_ = min(lp.max, rp.max)
            if v.value:
               assert v.value < max_, f'El segmento {leaf} no puede tener valor {v.value} pues los segmentos {lp.name} y {rp.name} tienen valores maximos de {lp.max} y {rp.max} respectivamente'
            else:
               assert v.min < max_, f'El segmento {leaf} no puede tener valor debido a que el mínimo valor esperado es {v.min} y el máximo es {max_}'
               v.max = max_
               if v.max == v.min:
                  v.value = v.max
            # print(v.left, v.name, v.right)
            if v.left:
               new_leafs.add(v.left)
            if v.right:
               new_leafs.add(v.right)
         leafs = new_leafs
      return True
   
   def min_propagation(self, from_ = None):
      # print('min from:',from_)
      
      if from_:
         leafs = [from_]
      else:
         leafs = self.leafs
      
      parents = set()
      for leaf in leafs:
         v = self.segments[frozenset(leaf)]
         if v.rparent:
            parents.add(v.rparent)
         if v.lparent:
            parents.add(v.lparent)
      
      while parents:
         # print(parents)
         new_parents = set()
         for parent in parents:
            v = self.segments[parent]
            # print(v.name, v.value)
            left = self.segments[v.left]
            right = self.segments[v.right]
            min_ = max(left.min, right.min)
            if v.value:
               assert v.value > min_, f'El segmento {parent} no puede tener valor {v.value} pues los segmentos {left.name} y {right.name} tienen valores {left.min} y {right.min} respectivamente'
               continue
            else:
               assert v.max >= min_, f'El segmento {parent} no puede tener valor debido a que el máximo valor esperado es {v.max} y el mínimo es {min_}'
               v.min = min_
               if v.min == v.max:
                  v.value = v.min
            if v.rparent:
               new_parents.add(v.rparent)
            if v.lparent:
               new_parents.add(v.lparent)
         parents = new_parents
      return True
   
   def is_valid(self):
      return self.max_propagation() ^ self.min_propagation()
   
class SemiValidateGeom:
   def __init__(self):
      print('''Antes de agregar valores de segmentos y angulos asegurate de colocar 
            todos los puntos y lineas''')
      self.lines = dict()
      self.points = set()
      self.angles = dict()
      self.segments = dict()
      self.segment_trees = dict()
      self.triangles = dict()
      self.theres_changes = False
   
   def new_line(self, key:str, points:list):
      assert len(set(points)) == len(points), 'No repitas puntos'
      for k, line in self.lines:
         intersec = set(line) & set(points)
         if len(intersec) >= 2:
            del self.lines[k]
            self.points = self.points - set(line)
            print(f'La linea {k}:{line} será remplazada por la linea {key}:{points} debido a que comparten los siguientes puntos {intersec}')
            break
      if key in self.lines.keys():
         f'La linea {key}:{self.lines[key]} ya existe, se remplazará por {points}'
      self.lines[key] = points
      self.segment_trees[key] = GeomSegmentTree(''.join(points))
      self.points = self.points | set(points)
      self.theres_changes = True
      
   def get_triangles(self):
      if self.theres_changes:
         for line in self.lines.values():
            non_collinear = self.points - set(line)
            pair_points = combinations(line, 2)
            for pair in pair_points:
               for point in non_collinear:
                  self.triangles[frozenset([*pair, point])] = SemiDummyTriangle(''.join([*pair, point]))
      return self.triangles
   
   def new_segment(self, name:str, value):
      
      if value <= 0:
         raise ValueError("Los lados deben ser positivos.")
      assert len(name) == 2, f'El segmento {name} tiene que tener 2 caracteres que sirvan de puntos.'
      for p in name:
         assert p in self.points, f'El punto {p} no es un punto existente'
      name = frozenset(name)
      
      self.segments[name] = value
      
   def propage_segments(self):
      if self.theres_changes:
         self.triangles = self.get_triangles()
         for seg, value in self.segments.items():
            for k, line in self.lines.items():
               intersec = set(line) & set(seg)
               if len(intersec) == 2:
                  key = k
                  break
            segment_tree = self.segment_trees[key]
            segment_tree.set_value(seg, value)
            
            triangles_with_seg = [frozenset(seg ^ set(point)) for point in self.points-set(self.lines[key])]
            for triangle in triangles_with_seg:
               self.triangles[triangle].segments[seg] = value
      self.theres_changes = False
      return True
   
   def new_angle(self, name, value, prop_of = None):
      assert len(name) == 3, "El nombre tiene que tener 3 caracteres que sirvan de puntos."
      assert value > 0, "Los angulos deben ser positivos."
      assert value < 180, "Los angulos deben ser menores a 180."
      assert set(name) & self.points == set(name), "Los puntos deven ser puntos existentes"
      
      if prop_of:
         if name in self.angles.keys():
            assert self.angles[name] == value, f'No se pudo propagar el valor {prop_of}:{self.angles[prop_of]} en el ángulo {name} por que tiene el valor asignado de {self.angles[name]}'
      
      self.angles[name] = value
      self.triangles[set(name)].angle[name[1]] = value
      self.theres_changes = True
   
   def related_angles_to(self, name:str):
      keys = []
      for k, line in self.lines.items():
         if len(set(line) & set(name)) == 2:
            if name[0] in line:
               keys.insert(0,k)
            else:
               keys.append(k)
      assert len(keys) == 2, f'No se pudieron encontrar las lineas'
      
      l1 = self.lines[keys[0]]
      l2 = self.lines[keys[1]]
      a,b,c = name
      b_indx = l1.index(b)
      
      if a in l1[:b_indx]:
         same_l1, opposite_l1 = l1[:b_indx], l1[b_indx+1:]
      else:
         same_l1, opposite_l1 = l1[b_indx+1:], l1[:b_indx]
      if c in l2[:b_indx]:
         same_l2, opposite_l2 = l2[:b_indx], l2[b_indx+1:]
      else:
         same_l2, opposite_l2 = l2[b_indx+1:], l2[:b_indx]
      
      same_val = []
      supplementaries = []
      
      for a in same_l1:
         for c in same_l2:
            same_val.append(''.join([a,b,c]))
         for c in opposite_l2:
            supplementaries.append(''.join([a,b,c]))
      
      for a in opposite_l1:
         for c in opposite_l2:
            same_val.append(''.join([a,b,c]))
         for c in same_l2:
            supplementaries.append(''.join([a,b,c]))
      
      return same_val, supplementaries
   
   def propagate_angles(self):
      if self.theres_changes:
         angles = deepcopy(self.angles.items())
         for name, value in angles:
            same_val, supplementaries = self.related_angles_to(name)
            for angle in same_val:
               self.new_angle(angle, value, prop_of=name)
            for angle in supplementaries:
               self.new_angle(angle, 180-value, prop_of=name)
      self.theres_changes = False
   
   def triangle_is_valid(self, triangle):
      name = triangle.name
      
      segment_values = [value for value in triangle.segments if value != None]
      angle_values = [angle for angle in triangle.angle.values() if angle != None]
      
      if len(segment_values == 3):
         m = max(segment_values)
         assert sum(segment_values) > 2*m, f'El triangulo {name}, con lados {segment_values}, no cumple la desigualdad del triangulo'
      
      if len(angle_values) == 2:
         assert sum(angle_values) < 180, f'Los angulos del triangulo {name}:{triangle.angle.items()} suman más de 180°'
      if len(angle_values) == 3:
         assert sum(angle_values) == 180, f'Los angulos del triangulo {name}:{triangle.angle.items()} no suman 180°'
   
   def is_valid(self):
      self.propage_segments()
      self.propagate_angles()
      
      for triangle in self.get_triangles():
         self.triangle_is_valid(triangle)
      
      return True