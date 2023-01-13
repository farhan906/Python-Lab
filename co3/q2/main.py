from graphics import circle,rectangle
from graphics.graphics3d import cuboid,sphere
a=int(input("parameter1="))
b=int(input("parameter2="))
c=int(input("parameter3="))
print("Area of the circle with radius",a, "=",circle.circlearea(a))
print("Perimeter of the circle with radius",a, "=",circle.circleperi(a))
print("Area of the rectangle with sides",a,b, "=",rectangle.rectarea(a,b))
print("Perimeter of the rectangle with sides",a,b, "=",rectangle.rectperi(a,b))
print("Area of the cuboid with sides",a,b,c, "=",cuboid.cuboidarea(a,b,c))
print("Perimeter of the cuboid with sides",a,b,c, "=",cuboid.cuboidperi(a,b,c))
print("Area of the sphere with radius",a, "=",sphere.spherearea(a))
print("Volume of the sphere with radius",a, "=",sphere.spherevolume(a))
