import sys
from os.path import abspath
from os.path import dirname
import chat


sys.path.insert(0, abspath(dirname(__file__)))
application = chat.app
