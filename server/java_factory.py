import os
os.environ['CLASSPATH'] = 'src/jar/symbolicPerseusIR.jar'

from jnius import autoclass

class JClass():
    JString = autoclass('java.lang.String')
    POMDP = autoclass('POMDP')
    OP = autoclass('OP')
    DDleaf = autoclass('DDleaf')
    DD = autoclass('DD')
    Utils = autoclass('Utils')
    Global = autoclass('Global')
