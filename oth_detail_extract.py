mylines = []
with open('resume.txt', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline.strip('\n'))

j = 0

length = len(mylines)
for i in range(length):
    if(mylines[i] == "EDUCATION"):
        while (j < length):
            if mylines[i + j] == "POSITIONS OF RESPONSIBILITY":
                break
            else:
                print(mylines[i + j])
            j += 1

j = 0

for i in range(length):
    if(mylines[i] == "COURSEWORK INFORM ATION"):
        while (j < length):
            if mylines[i + j] == "Please note if any item is marked as '!' the same is not verified by CDC, IIT Kharagpur.":
                break
            else:
                print(mylines[i + j])
            j += 1
