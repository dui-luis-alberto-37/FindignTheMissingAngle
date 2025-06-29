from collections import defaultdict

class GeometicRepresentation:
    def __init__(self, name: str = None):
        #self.name = name
        self.lines_points = defaultdict(list)
        self.points_lines = defaultdict(list)
        
        self.lasts = {
            "line": 0,
            "point": 0,
        }
        
    
    def add_line(self, nline: list,):
        """Add a line to the geometric representation."""
        for line in self.lines_points.values():
            if nline == line:
                print(f"Line {line} already exists.")
                return None

        last_l = self.lasts["line"]
        self.lines_points[f'l{last_l}'] = nline
        
        self.lasts["line"] += 1
        
        for point in nline:
            self.points_lines[point].append(f'l{last_l}')
            
            

    def triangle_internal_sum(triangle):
        """Asserst that the internal angle sum of a triangle is 180 degrees."""
        x, y, z = triangle
        return x + y + z == 180  
        
    
    def get_triagles(self):
        """Get the triangles from the geometric representation."""
        triangles = []
        for line in self.lines:
            pass
        return triangles
        