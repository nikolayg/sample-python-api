from server.instance import server
import sys, os

# Need to import all resources
from resources.book import *

# Ensure current folder is on the path
sys.path.insert(0, os.path.abspath('.'))

if __name__ == '__main__':
    server.run()