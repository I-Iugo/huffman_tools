import argparse
from utils.compression import encodage
from utils.decompression import decodage
from utils.file_manager import *

"""
This is the simple cli. For understand better read
https://docs.python.org/3/library/argparse.html
"""

parser = argparse.ArgumentParser(description='Compress Huffman tool')
parser.add_argument('-c',
                    '--compress',
                    help='compress file.txt',
                    action='store_true')
parser.add_argument('-d',
                    '--decompress',
                    help='decompress file.txt',
                    action='store_true')
parser.add_argument('file', metavar='F', type=str)

args = parser.parse_args()
if args.compress:
    content = inputContent(args.file)
    compress = encodage(content)
    file_compressed = output(compress, "leHorlaEncode.txt")
    print('Your content has compressed in:', file_compressed)
elif args.decompress:
    content = inputContent(args.file)
    decompress = decodage(content)
    file_decompressed = output(decompress, "leHorlaDecode.txt")
    print('Your content is in:', file_decompressed)
