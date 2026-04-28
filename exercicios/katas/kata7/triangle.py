class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5
    
    def maior_area(self, outro):
        if self.area() > outro.area():
            return "X tem a maior area"
        else:
            return "Y tem a maior area"