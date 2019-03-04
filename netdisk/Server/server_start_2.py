import sys
import os

from core_server import src_other_server
path = os.path.dirname(__file__)
sys.path.append(path)


if __name__ == '__main__':
    src_other_server.run()