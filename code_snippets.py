import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# argparse
 

import argparse

parser = argparse.ArgumentParser(
               description=__doc__,
               formatter_class=argparse.RawDescriptionHelpFormatter)

 

# required argument
parser.add_argument("-s",'--source',
                        type=str,
                        default=ALL_PROD_DIR,
                        nargs='?',
                        help='source path, where the dataset is available')
parser.add_argument('-r',"--random",
                        action='store_true',
                        help='whether created data should be random file \
                            or not')
args = parser.parse_args()
