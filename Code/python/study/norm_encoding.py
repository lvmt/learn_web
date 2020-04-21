#!/usr/bin/env python2
# encoding: utf-8
'''\033[1;3;32m
    normalizing file with multiple encodings to utf8
\033[0m'''
import sys
import chardet


__author__ = 'suqingdong'
__version__ = '1.0'


def main(infile=None, outfile=None):

    infile = sys.stdin if infile in ('-', 'stdin') else open(infile)
    outfile = sys.stdout if outfile in ('-', 'stdout') else open(outfile, 'w')

    with infile as inf, outfile as out:
        for line in inf:
            enc = chardet.detect(line)['encoding'] or 'gbk'
            line = line.decode(enc)
            out.write(line)


if __name__ == '__main__':

    import argparse

    epilog = '''
\033[36mexample:
  %(prog)s input.txt    
  %(prog)s input.txt -o output.txt 
  cat input.txt | %(prog)s
  cat input.txt | %(prog)s -o output.txt 

\033[33mcontact: {__author__}@novogene.com
'''.format(**globals())

    parser = argparse.ArgumentParser(
	    prog='norm_encoding',
	    description=__doc__,
	    epilog=epilog,
	    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
	    'infile',
	    nargs='?',
	    default='stdin',
	    help='the input file which maybe contains multiple encodings [default: %(default)s]')

    parser.add_argument(
	    '-o',
	    '--outfile',
	    default='stdout',
	    help='the output file [default: %(default)s]')

    if (len(sys.argv) == 1) and sys.stdin.isatty():
        parser.print_help()
        exit()

    args = vars(parser.parse_args())

    main(**args)

