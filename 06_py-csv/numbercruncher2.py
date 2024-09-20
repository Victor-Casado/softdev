#Victor Casado
#The Flying Mice
#SoftDev
#K06 -- Divining Destiny with second method
#2024-09-18
#time spent: .3 hours
import random as r

f = open("occupations.csv", "r")
string = f.read()

list = string.split("\n")
list = list[1:len(list)-2] #removes example row, total row, and new line row

names = []
nums = []
counter = 0

for i in range(len(list)):
    if(list[i][0] == "\""):
        indexcomma = list[i][1:].index("\"") + 2
        name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
        num = list[i][indexcomma + 1:]
    else:
        split = list[i].split(",")
        name = split[0]
        num = split[1]
    names.append(name)
    nums.append(float(num))
    counter += 1
    #print(str(counter) + ": " + name)
#print(names)
#print(nums)
#print(dict)
print(r.choices(names, nums)[0])
