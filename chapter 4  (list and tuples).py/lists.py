# what is list?

# list is a container to store a set of values of any data type in it.

             #create  alist using []
a=[1,2,3,4,5,6]
a[0]=81              # replacing 1 with 81
print(a)
a[0]=1
print(a)
print(a[2])           #prints 3rd element

b=["ashar","saad","jiya"]
print(b[0 :3])

l1=[1,2,3,4,5,69,8,7,2,4545,6]
l1.sort()                                  #l1.sort() re arranges assending order
print(l1)

l1.reverse()
print(l1)

l1.append(25)                               #adds 25 to end of the list       
print(l1)                                   

l1.pop(2)
print(l1)                   #removes 3rd index from the list

l1.remove(69)               #removes 69 from the given list
print(l1) 


b.append("zafar")
print(b)


alist=[1,2,3,4]
blist=[1,2,4,3]
print(alist+blist)           #add two lists together
alist.extend(blist)       #does the same work as + does

print(alist)
                         
#totla

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


                            # how to replace two variables




variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1





                                            #




# step 1:
Beatles = []
print("Step 1:", Beatles)

# step 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3:
for members in range(2):
    Beatles.append(input("New band member: "))
print("Step 3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5:
Beatles.insert(0, "RingoStarr")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))