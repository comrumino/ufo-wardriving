from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import sys, os.path

def getQIcon(name):
    return QIcon(repr(os.path.dirname(\
    os.path.realpath(sys.argv[0]))).replace("\\\\","/")\
    .replace("\'","")+"/pics/"+name)
