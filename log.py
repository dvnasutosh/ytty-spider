import logging
import traceback
from sys import exc_info


class Log:

    def __init__(self, levelName: str = 'root'):
        format_basic = '%(name)s %(levelname)s %(asctime)s : %(message)s'
        format_trail = '%(name)s %(levelname)s %(asctime)s  :  %(message)s \n\t%(filename)s %(funcName)s ln:(%(lineno)s)'

        logging.info('setting basic config for log at' + levelName(str))
        # Initiaing log
        logging.basicConfig(filename='root.log', level=logging.info, format=format_basic)

        self.l = logging.getLogger(levelName)
        self.l.setLevel(logging.INFO)
        self.l.addHandler(logging.FileHandler('log.log').setFormatter(format_basic))

        logging.info('initiated procession logger')

        self.trail = logging.getLogger(levelName)
        self.trail.setLevel(logging.INFO)
        self.trail.addHandler(logging.FileHandler('log.log').setFormatter(format_basic))
        logging.info('initiated procession logger')

    def getdev(self, s):
        dev = logging.getLogger(s)
        dev.setLevel(logging.DEBUG)
        dev.addHandler(logging.FileHandler(filename='dev.log').setFormatter('%(name)s %(levelname)s %(lineno)s : %(message)s'))
        return dev
    def i(self,msg):
        self.l.info(msg)
        self.trail.info(msg)
    def e(self,msg):
        self.l.error(msg)
        self.trail.error(msg)
    def c(self,msg):
        self.l.critical(msg)
        self.trail.critical(msg)


    def exc(self,msg):
        self.l.exception(msg,exc_info=True)
        self.trail.exception(msg,exc_info=True)
