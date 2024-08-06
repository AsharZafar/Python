#dictionary is a collection of key-valur pairs
#it is mutable
#it is unordered
#it is indexed
#you cannot duplicate keys



#creating nested dictionary

mydict= {
    "fast":"in a quick manner",
    "ashar":"is becoming a coder",
    "marks":"lag gye",
    "another dict":{"ashar":"s/0 zafar"}           #nested dictionary
}
print(mydict["fast"])
print(mydict["ashar"])
print(mydict["marks"])
print(mydict["another dict"]["ashar"])

mydict["marks"]=[25,30]                              #changes marks values

print(mydict)


                 #methods of dictionary

print(mydict.keys())              #prints keys in the form of list i.e left one's
print(mydict.values())              #prints values in the form of list i.e right one's

print(type(mydict))                     #not a list type but it is a   <class 'dict'>

print(list(mydict.keys()))              # keys displayed in the form of  list \
print(list(mydict.values()))            #displays values in the form of a list


print(mydict)

updated_dict= {
    'ashar':'goodboy',
    'saad':'mr.torphor'
}
mydict.update(updated_dict)                         #updates the previous dict
print(mydict)                                       #added to disk

print(mydict.get(ahsar.z))                          #will display none as if ashar.z is not present in the dictionary


#print(mydict(ahsar.z))                               #will display error as ashar.z is not present in the dictionary           