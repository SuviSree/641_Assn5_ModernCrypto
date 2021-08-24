f = open("output.txt","r")
g = open("new_output.txt","w")

for line in f:
    
    line2 = line.replace('\n', ' ')

    g.write(line2)
