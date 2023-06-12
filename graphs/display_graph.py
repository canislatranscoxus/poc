'''
Here we use graphviz library to create and display graphs

links:
    https://pypi.org/project/graphviz/
'''

import graphviz

'''
valid formats = pdf, svg, png
'''
dot = graphviz.Digraph(comment='The Round Table', format = 'pdf' )

dot.node('A', 'King Arthur')  
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')


print( dot.source )

dot.render('/home/art/git/poc/graphs/round-table.gv', view=True)
# 'round-table.gv.pdf'