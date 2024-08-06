from math import sqrt as square
def area_of_triangle(length,bredth,unit="meters"):
    area=1/2*(length*bredth)
    return area , unit
  
def check_right_triangel(a,b,c):
    #pythagoras theorum
    #H2 =b^2 +p^2
    if (square(c)==square(b)+square(a)):
        print("triangle is a right triangle")
    else:
        print("triangle is not a right triangle")


print('Mike'>"Mikey")

print(ord('c')-ord('a'))
print(chr(ord('z')-2))
try:
    print("5"/0)
except ArithmeticError:
    print("err")
except ZeroDivisionError:
    print("2")
except:
    print("some")