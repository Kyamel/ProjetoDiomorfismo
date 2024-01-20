import numpy as np
from numpy import ndarray
import warnings

class Point:
    def __init__(self, x, y):
        if not (np.isscalar(x) and np.isscalar(y)):
            raise TypeError("The arguments x and y must be scalar numbers supported by NumPy.")

        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
class ArcOfCircle:
    def __init__(self, begin_point, center_point, end_point):
        self._validate_point(begin_point, "begin_point")
        self._validate_point(end_point, "end_point")
        self._validate_point(center_point, "center_point")

        self.begin_point = begin_point
        self.end_point = end_point
        self.center_point = center_point

    def _validate_point(self, point, point_name):
        if not isinstance(point, Point):
            raise TypeError(f"{point_name} should be an instance of Point")

    def __repr__(self):
        return f"Arc({self.begin_point}, {self.center_point}, {self.end_point})"

    def radius(self):
        radius_begin = np.sqrt((self.begin_point.x - self.center_point.x)**2 + (self.begin_point.y - self.center_point.y)**2)

        radius_end = np.sqrt((self.end_point.x - self.center_point.x)**2 + (self.end_point.y - self.center_point.y)**2)

        if radius_begin == radius_end:
            return radius_begin
        else:
            raise ValueError("Object should be an arc of circle with equal x and y radii.")
        
    def begin_angle(self):
        angle = (np.arctan2(self.begin_point.y, self.begin_point.x) + 2 * np.pi) % (2 * np.pi)
        return angle
    
    def end_angle(self):
        angle = (np.arctan2(self.end_point.y, self.end_point.x) + 2 * np.pi) % (2 * np.pi)
        return angle
    
    def angle_in_between(self):
        #só retorna valores positivos
        angle = self.end_angle() - self.begin_angle()
        if angle < 0.0:
            return (np.pi*2) + angle
        else:
            return angle

class MultiPoint:
    def __init__(self, x_values, y_values):
        self._validate_values(x_values, 'x')
        self._validate_values(y_values, 'y')
        self.x = x_values
        self.y = y_values
        self.points = [Point(x, y) for x, y in zip(self.x, self.y)]

    def __repr__(self):
        return f"MultiPoints{self.points}"
    
    def _validate_values(self, values, values_name):
        if not isinstance(values, ndarray):
            raise TypeError(f"{values_name} should be an instance of np.array")

    def get_point(self, index):
        if 0 <= index < len(self.points):
            return self.points[index]
        else:
            raise IndexError("Index out of range")
    
    def get_last_point(self):
        if len(self.points) > 0:
            return self.points[-1]
        else:
            warnings.warn("Trying to get point from an empty list.", UserWarning)
            return None

    def get_first_point(self):
        if len(self.points) > 0:
            return self.points[0]
        else:
            warnings.warn("Trying to get point from an empty list.", UserWarning)
            return None

    def add_point(self, x, y):
        if not (np.isscalar(x) and np.isscalar(y)):
            raise TypeError("The arguments x and y must be scalar numbers supported by NumPy.")
        else:
            self.points.append(Point(x, y))
            self.x = np.append(self.x, x)
            self.y = np.append(self.y, y)

    def remove_point(self, index):
        if 0 <= index < len(self.points):
            del self.points[index]
            self.x = np.delete(self.x, index)
            self.y = np.delete(self.y, index)
        else:
            raise IndexError("Index out of range")

    def remove_first_point(self):
        if len(self.points) > 0:
            del self.points[0]
            self.x = np.delete(self.x, 0)
            self.y = np.delete(self.y, 0)
        else:
            warnings.warn("Trying to remove point from an empty list.", UserWarning)
            return None

    def remove_last_point(self):
        if len(self.points) > 0:
            del self.points[-1]
            self.x = np.delete(self.x, -1)
            self.y = np.delete(self.y, -1)
        else:
            warnings.warn("Trying to remove point from an empty list.", UserWarning)
            return None

    def get_num_points(self):
        return len(self.points)

class MultiArcOfCircle:
    def __init__(self, begin_points, center_points, end_points):
        self._validate_points(begin_points, "begin_point")
        self._validate_points(end_points, "end_point")
        self._validate_points(center_points, "center_point")
        
        self.begin_points = begin_points
        self.center_points = center_points
        self.end_points = end_points

        self.arcs = [ArcOfCircle(begin, center, end) for begin, center, end in zip(begin_points.points, center_points.points, end_points.points)]

    def __repr__(self):
        return f"MultiArc{self.arcs}"
    
    def _validate_points(self, points, points_name):
        if not isinstance(points, MultiPoint):
            raise TypeError(f"{points_name} should be an instance of MultiPoint")

    def add_arc(self, begin, center, end):
        self._validate_points(begin, "begin_point")
        self._validate_points(end, "end_point")
        self._validate_points(center, "center_point")
        
        self.begin_points.add_point(begin.x, begin.y)
        self.center_points.add_point(center.x, center.y)
        self.end_points.add_point(end.x, end.y)

        self.arcs.append(ArcOfCircle(begin, center, end))

    def get_arc(self, index):
        if 0 <= index < len(self.arcs):
            return self.arcs[index]
        else:
            raise IndexError("Index out of range")
        
    def get_last_arc(self):
        if len(self.arcs) > 0:
            return self.arcs[-1]
        else:
            warnings.warn("Trying to get arc from an empty list.", UserWarning)
            return None

    def get_first_arc(self):
        if len(self.arcs) > 0:
            return self.arcs[0]
        else:
            warnings.warn("Trying to get arc from an empty list.", UserWarning)
            return None

    def remove_arc(self, index):
        if 0 <= index < len(self.arcs):
            del self.arcs[index]
            self.begin_points.remove_point(index)
            self.center_points.remove_point(index)
            self.end_points.remove_point(index)
        else:
            raise IndexError("Index out of range")

    def remove_first_arc(self):
        if len(self.arcs) > 0:
            del self.arcs[0]
            self.begin_points.remove_first_point()
            self.center_points.remove_first_point()
            self.end_points.remove_first_point()
        else:
            warnings.warn("Trying to remove point from an empty list.", UserWarning)
            return None

    def remove_last_arc(self):
        if len(self.arcs) > 0:
            del self.arcs[-1]
            self.begin_points.remove_last_point()
            self.center_points.remove_last_point()
            self.end_points.remove_last_point()
        else:
            warnings.warn("Trying to remove point from an empty list.", UserWarning)
            return None

    def get_num_arcs(self):
        return len(self.arcs)

# Exemplo de uso
"""

x1 = np.array([1, 0, -1])
y1 = np.array([0, 1, 0])
x2 = np.array([0, 0, 0])
y2 = np.array([0, 0, 0])
x3 = np.array([0, -1, 0])
y3 = np.array([-1, 0, 1])

pi = MultiPoint(x1, y1)
pc = MultiPoint(x2, y2)
pe = MultiPoint(x3, y3)

print("---------Ponto------------")

p = Point(3, 4)
print(p)
print(p.x)
print(p.y)

print("----------MultiPonto----------")

print(pi)
print(pi.x)
print(pi.y)
p1 = pi.get_first_point()
print(p1)
print(p1.x)
l = pi.get_num_points()
print(l)
pi.remove_last_point()
print(pi)
print(pi.x)
print(pi.y)
pi.add_point(4, 5)
print(pi)
print(pi.x)
print(pi.y)

print("------------Arcos--------------")

arco = ArcOfCircle(p, p, p)

print(arco)
print(arco.begin_point)
print(arco.center_point.x)
print(arco.end_point.y)
a = arco.angle_in_between()
print(a)

print("------------MultiArcos----------")

arcos = MultiArcOfCircle(pi, pc, pe)
print(arcos)
f_arc = arcos.get_last_arc()
print(f_arc.begin_point)
print(arcos.get_num_arcs())
angle = np.array([])

for i in range(0, arcos.get_num_arcs()):
    arco = arcos.get_arc(i)
    angle = np.append(angle, arco.angle_in_between())

print(angle)

print(arcos.begin_points)

"""