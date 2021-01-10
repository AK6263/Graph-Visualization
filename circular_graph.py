import math
# We will be generating the gv file here and executing it separately
# using neato . First we will get the list of the nodes
seq_name= []
with open("rosalind_grph.txt","r") as sequences:
    line = sequences.readline().strip()
    while line != "":
        if line[0] == ">":
            seq_name.append(line[1:])
            line = sequences.readline().strip()
            print(seq_name)
            print(line)
len(seq_name)
sequences.close()


graph_circle = open("coordinates.txt","w")
# writting the init portion

graph_circle.write("digraph G {\n")
graph_circle.write("    layout='neato'\n")

# Calculating the nodes positions
radius = 50
n_nodes = len(seq_name)
for i,n in enumerate(seq_name):
    x = math.cos((2*math.pi*(i+1))/n_nodes)*radius
    y = math.sin((2*math.pi*(i+1))/n_nodes)*radius
    graph_circle.write("    {}[label = {}, pos = {}, shape = {}]".format(str(i), str(x)+","+str(y) + "!", "square"))
graph_circle.write("}\n")