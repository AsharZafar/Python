import trignometry as tri
tri_area, unit =tri.area_of_triangle(10, 15)
print(f"area of triangle is {tri_area} {unit}")
if tri_area>100:
    print("it is a big triangle")
else:
    print("triangle is a small triangle")



print(tri.check_right_triangel(12, 20, 60))