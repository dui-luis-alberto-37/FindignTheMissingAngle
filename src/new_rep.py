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
      if value >= 360:
         raise ValueError("Los angulos deben ser menores a 180.")
      else:
         self.angles[name] = value
   
   def new_segment(self, name:str, value):
      if value <= 0:
         raise ValueError("Los lados deben ser positivos.")
      name = frozenset(name)
      self.segments[name] = value