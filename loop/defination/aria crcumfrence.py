import math
def crecle(r):
    area=math.pi*r**2
    cercufrence=2*math.pi*r
    return area, cercufrence

area, circumference = crecle(5)
print("Area of the circle:", f"{area:.2f}", end=" ")
print("Circumference of the circle:", f"{circumference:.2f}")