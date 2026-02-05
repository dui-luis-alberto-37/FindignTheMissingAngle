from Figures import Fig1_V4, Fig2_V4, Fig1_V2, Fig2_V2, Fig1_V3, Fig2_V3
from new_rep import SemiDummyTriangle as Triangle
from itertools import combinations


class SearchGraph:
   def __init__(self, root, Fig):
      self.root = root
      self.Fig = Fig
      lines = Fig.lines
      angles = Fig.angles
      triangles = Fig.triangles
      
   def neighbors(self, angle):
      vertex_neighbours = []
      triangles_neigbours = []
      
      center = angle[1]
      lines = self.lines_with(center)
      extremes = [set(l[0],l[1]) - set(center) for l in lines]
      for l1, l2 in combinations(extremes):
         for e in ext1: 
         
      
   
   def lines_with(self, point):
      lines = []
      for line in self.lines.values():
         if point in line:
            lines.append(point)
      return lines
      
   def identify_line(self, name):
      for k, line in self.Fig.lines.items():
         if len(set(line) & set(name)) == 2:
            return k
   
   def 

def Search_V4(angle, Fig):
   steps = 0
   
   
   
   
   res = None
   return res