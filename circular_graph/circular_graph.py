import math
# We will be generating the gv file here and executing it separately
# using neato . First we will get the list of the nodes
seq_name= []
with open("../fasta files/rosalind_grph.txt","r") as sequences:
    line = sequences.readline().strip()
    while line != "":
        if line[0] == ">":
            seq_name.append(line[1:])
        line = sequences.readline().strip()
print(len(seq_name))
sequences.close()


graph_circle = open("coordinates.gv","w")
# writting the init portion

graph_circle.write("digraph G {\n")
graph_circle.write("    layout=\"neato\"\n")
graph_circle.write("    node [shape=circle]\n")
# graph_circle.write("    overlap=False\n")
shape = "circle"
# Calculating the nodes positions
radius = 1000
n_nodes = len(seq_name)
for i,n in enumerate(seq_name):
    x = math.cos((2*math.pi*(i+1))/n_nodes)*radius
    y = math.sin((2*math.pi*(i+1))/n_nodes)*radius
    graph_circle.write("    {}[label = \"{}\", pos = \"{},{}!\", shape = \"{}\"]\n".format(str(i+1),n[-4:], str(round(x,10) ),str(round(y,10)),shape ))
# 2-> 27
with open("../submission_3.txt","r") as relations:
    line = relations.readline().strip()
    while line!="":
        nodes = line.split(",")
        i = seq_name.index(nodes[0]) + 1
        j = seq_name.index(nodes[1]) + 1
        label = nodes[2]
        graph_circle.write("    {} -> {} [label = {}]\n".format(str(i),str(j),label))
        line = relations.readline().strip()
graph_circle.write("}\n")
graph_circle.close()