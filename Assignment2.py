'''
#Program 1.1: Concat first and last name

def full_name(fname, lname):
    return First_name + ' ' + Last_name
def string_alternative(full_name):
    op_string1 = ''
    for i in range(len(full_name)):
        if i == 0:
            x = full_name[i]
            op_string1 = op_string1+x
        elif i>0 and i%2==0:
            x = full_name[i]
            op_string1 = op_string1+x   
    return op_string1

First_name = input("First name:")
Last_name = input("Last name:")
full_name = full_name(First_name,Last_name)
print("Final op:", full_name)
op_string1 = string_alternative(full_name)
print("Alternate string:" , op_string1)

'''

#Prog 3: Word count from input file
ip_file = open("C:/Users/sruja/OneDrive/Desktop/Neural Network/Neural-git/Assignments/ipfile.txt", "r")
op_file = open("C:/Users/sruja/OneDrive/Desktop/Neural Network/Neural-git/Assignments/opfile.txt", "w")
info = {}
for line in ip_file:
    op_file.write(line)
    newline = line.split()
    for x in newline:
        if(info.get(x)==None):
            info[x]=1
        else:
            info[x] = info[x] + 1
            
op_file.write("Word_Count : ")
for key, value in info.items(): 
        op_file.write('%s:%s\n' % (key, value))
print("Output file created")

# Prog 4: Convert given height from inches to centimeters
def convertint_into_cm(value):
    return value*2.54
Ip = input("enter height : ")
height_split = Ip.split()
oplist = []
for i in height_split:
    value = int(i)
    oplist.append(convertint_into_cm(value))
print("output: ",oplist)