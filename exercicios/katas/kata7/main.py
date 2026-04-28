from triangle import Triangle

x = Triangle(3.0, 4.0, 5.0)
y = Triangle(7.50, 4.50, 4.02)

print(f"{x.area():.2f}")
print(f"{y.area():.2f}")
print(x.maior_area(y))