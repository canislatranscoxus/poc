'''
Here we use graphviz library to create and display graphs

links:
    https://pypi.org/project/graphviz/
'''

import graphviz

'''
valid formats = pdf, svg, png
'''

def g1():
    dot = graphviz.Digraph( comment='g1', format = 'pdf' )

    dot.node('A', 'A')  
    dot.node('B', 'B')
    dot.node('C', 'C')
    dot.edges( ['AB', 'BC'])

    print( dot.source )
    dot.render( '/home/art/git/poc/graphs/g1.gv', view=True )

def g2():
    dot = graphviz.Digraph( comment='g2', format = 'pdf' )

    dot.node('A', 'A')  
    dot.node('B', 'B')
    dot.node('C', 'C')
    dot.edges(['AB', 'AC'])


    print( dot.source )
    dot.render( '/home/art/git/poc/graphs/g2.gv', view=True )


def g3():
    dot = graphviz.Digraph( comment='g2', format = 'pdf' )

    dot.node('A', 'A')  
    dot.node('B', 'B')
    dot.node('C', 'C')
    dot.edges(['AC', 'BC'])

    print( dot.source )
    dot.render( '/home/art/git/poc/graphs/g3.gv', view=True )

g1()
g2()
g3()