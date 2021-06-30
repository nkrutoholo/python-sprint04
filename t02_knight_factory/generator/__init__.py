import logging
import sys
from . import names, titles


logging.basicConfig(stream=sys.stdout, \
                    format='..::Knight Generator::.. %(process)d-%(levelname)s-%(message)s', \
                    level=logging.INFO)
