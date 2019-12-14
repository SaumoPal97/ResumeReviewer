mylines = []
with open('resume.txt', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)

print("Name: ", end="")
for c in mylines[0]:
    if c == "|":
        break;
    else:
        print(c, end="")
