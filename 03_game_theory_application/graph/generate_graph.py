from graphviz import Graph
from graphviz import Digraph
graph_engine = 'sfdp'

G = Graph(format='pdf', engine=graph_engine)
G.attr('node', shape='circle', color='black')

G.edge('1', '2', label='0.5')
G.edge('1', '3', label='0.9')
G.edge('2', '4', label='0.3')
G.edge('2', '5', label='0.2')
G.edge('3', '6', label='0.4')
G.edge('4', '6', label='0.7')
G.edge('5', '6', label='0.8')

G.render('sample_graph')

H = Digraph(format='pdf', engine=graph_engine)
H.attr('node', shape='circle', color='black')

H.edge('1', '2', penwidth='3', color='red', label='0.5')
H.edge('1', '3', penwidth='3', color='blue', style='dashed', label='0.9')
H.edge('2', '4', penwidth='3', color='purple', style='dotted', label='0.3')
H.edge('2', '5', penwidth='3', color='red', label='0.2')
H.edge('3', '6', penwidth='3', color='blue', style='dashed', label='0.4')
H.edge('4', '6', penwidth='3', color='purple', style='dotted', label='0.7')
H.edge('5', '6', penwidth='3', color='red', label='0.8')

H.node('1', shape='circle', style='filled', color='green')
H.render('sample_graph_path')
