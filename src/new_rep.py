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
         intesec = set(line) & set(points)
         if len(intesec) >= 2:
            del self.lines[k]
            for point in line:
               self.points = self.points - set(line)
            print(f'La linea {k}:{line} será remplazada por la linea {key}:{points} debido a que comparten los siguientes puntos {intesec}')
            break
      
      self.lines[key] = points
      for point in points:
         self.points.add(point)
         
   def new_segment(self, name:str, value):
      if value <= 0:
         raise ValueError("Los lados deben ser positivos.")
      name = frozenset(name)
      self.segments[name] = value
      
      triangles_with_seg = [frozenset(name ^ set(point)) for point in self.points-set(name)]
      for triangle in triangles_with_seg:
         self.triangles[triangle] = SemiDummyTriangle(triangle)
         self.triangles[triangle].segments[name] = value
   
   def new_angles(self, name:str, value):
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
   
   
