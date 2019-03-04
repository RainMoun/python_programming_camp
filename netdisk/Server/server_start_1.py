import sys
import os

from core_server import src
path = os.path.dirname(__file__)
sys.path.append(path)


if __name__ == '__main__':
    src.run()

