                                  #slicing
                                



                                 #[1:4:1]    = first , last , spacing


name='asharzafar'
d=name[:4:1]      #from start to four characters
print(d)

name="mynameisahsar"
c=name[0::2]       # from start to last characters with gaping of one
print(c)


name="mynameisahsar"
c=name[0::3]       # from start to last characters with gaping of two
print(c)

print(len(name))

print(name [:13])    #from srart to last without any gap
print(name[0:])      #from start to last



                          #slicing of lists

num=[1,2,3,4,5,6,7,8,9,10]
print(num[5])             #index is printed

print(num[4:5])           #this time a 5 of a list is printed

                         #copy with slicing

copy=num[0:10]
print(copy)

                    #pass by refrence

#both have the same id
#a and b
a=10
c=10
b=a
print(id(a))
print(id(b))




name="asharzafar"
print(name*2)            #writes name 2 times

