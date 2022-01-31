
class Dot_3d:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    def __add__(self, other):
        if isinstance(other, Dot_3d):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
        else:
            x = self.x + int(other)
            y = self.y + int(other)
            z = self.z + int(other)
        return Dot_3d(x, y, z)

    def __mul__(self, i: int):
        x = self.x * i
        y = self.y * i
        z = self.z * i
        return Dot_3d(x, y, z)

    def __sub__(self, other):
        if isinstance(other, Dot_3d):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
        else:
            x = self.x - int(other)
            y = self.y - int(other)
            z = self.z - int(other)
        return Dot_3d(x, y, z)

    def __truediv__(self, i: int):
        x = self.x / i
        y = self.y / i
        z = self.z / i
        return Dot_3d(x, y, z)

dot1 = Dot_3d(1, 2, 5)
dot2 = Dot_3d(2, 3, 0)
print(dot1+dot2)
print(dot1+5)
print(dot1*5)
print(dot1/5)


