import sys

import os

INTERP = os.path.expanduser("/var/www/u0811189/data/www/intelligent-system.online/flaskenv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from skud import application