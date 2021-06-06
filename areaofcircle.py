def area_circle(r):
    area = 3.14 * (r**2)
    return area
r = int(input("Input the radius of the circle : "))
print(f"The area of the circle with radius {r} is : {area_circle(r)}")
