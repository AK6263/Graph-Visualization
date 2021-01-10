from graphviz import Digraph

g = Digraph('Overlap Graph for 3', filename="overlap_graph_3.gv")

# g.attr(rankdir='LR', size='8,5')

g.attr('node', shape='circle')
with open("submission_3.txt","r") as graph:
    line = graph.readline().strip()
    while line != "":
        nodes = line.split(",")
        g.edge(nodes[0][-4:],nodes[1][-4:],label = nodes[2])
        line = graph.readline().strip()
g.attr(overlap='false')
g.view()
# g.render("Overlapgraph", 'png')