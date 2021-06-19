class Vector2:

    def __init__(self, coordnates, lenght=1) -> None:
        self.x, self.y = coordnates
        self.lenght = lenght
    
    def convert(self, x, y):
        return Vector2((x+self.x, y+self.y))
    
    def __eq__(self, vecteur) -> bool:
        return self.lenght == vecteur.lenght
    
    def __lt__(self, vecteur) -> bool:
        return self.lenght < vecteur.lenght
    
    def __str__(self):
        return f"Vector(x = {self.x}, y = {self.y}, lenght={self.lenght})"

    def __mul__(self, nbr):
        return Vector2((self.x * nbr, self.y * nbr), self.lenght)
    
    def __truediv__(self, nbr):
        return Vector2((self.x // nbr, self.y // nbr), self.lenght)
    
    def __neg__(self):
        return Vector2((self.x * -1, self.y * -1), self.lenght)

    @property
    def indice(self):
        return (self.x, self.y)

if __name__ == "__main__":
    print(Vector2((0, 0), 1) > Vector2((-1, 0), 2))



    """
    
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    
    
    """
