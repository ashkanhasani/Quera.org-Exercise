class Foo:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value >= 0:
                # If the number is non-negative, store the two digits on the right side
                self._x = value % 100
            else:
                # If the number is negative, set x to -1
                self._x = -1
        else:
            raise ValueError("Value must be of type int")

