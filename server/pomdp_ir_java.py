import os
os.environ['CLASSPATH'] = '/pkg/pomdp-ir/jar/symbolicPerseusIR.jar'

from jnius import autoclass

pomdpfile = '/pkg/pomdp-ir/models/patrol.dat'

print('Before instatiation Solver')
Solver = autoclass('Solver')
print('Instatiated Solver')
Solver.main([pomdpfile,'-g'])
