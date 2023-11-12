# import graphviz  # doctest: +NO_EXE
# dot = graphviz.Digraph(comment='The Round Table')
# dot  #doctest: +ELLIPSIS

# dot.node('A', 'King Arthur')  # doctest: +NO_EXE
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# print(dot.source)  # doctest: +NORMALIZE_WHITESPACE +NO_EXE

# # doctest_mark_exe()
# dot.render('doctest-output/round-table.dv')
###

import graphviz

dot = graphviz.Digraph('round-table', comment='The Round Table')  

dot.node('A', 'King Arthur')  
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

dot.render(directory='doctest-output')
###
# import graphviz
# dot = graphviz.Graph(name='spam', directory='doctest-output')

# dot.node('A', 'King Arthur')  # doctest: +NO_EXE
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# dot.render(format='png').replace('\\', '/')
# dot.render(outfile='spam.svg').replace('\\', '/')

###
# import graphviz

# h = graphviz.Graph('hello', format='svg')  
# h.edge('Hello', 'World')
# h.pipe(format='pdf')[:4]
# print(h.pipe(encoding='utf-8'))  