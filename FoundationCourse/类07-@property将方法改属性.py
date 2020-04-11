class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


c1 = C()
print(c1.x)
c1.x = 'hello'
print(c1.x)
