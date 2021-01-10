from graphviz import Digraph

g = Digraph('sample', filename="sample.gv")

g.attr(rankdir='LR', size='8,5')

g.attr('node', shape='circle')

g.edge("TOYOT", "YOTA", label="3")

g.view()
g.render("sample.png", 'png')