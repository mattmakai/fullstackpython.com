# vim:ts=4 sw=4 expandtab softtabstop=4
from __future__ import print_function
import optparse
import locale
import os
import sys
import warnings

from unidecode import unidecode

PY3 = sys.version_info[0] >= 3

def fatal(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)

def main():
    default_encoding = locale.getpreferredencoding()

    parser = optparse.OptionParser('%prog [options] [FILE]',
            description="Transliterate Unicode text into ASCII. FILE is path to file to transliterate. "
            "Standard input is used if FILE is omitted and -c is not specified.")
    parser.add_option('-e', '--encoding', metavar='ENCODING', default=default_encoding,
            help='Specify an encoding (default is %s)' % (default_encoding,))
    parser.add_option('-c', metavar='TEXT', dest='text',
            help='Transliterate TEXT instead of FILE')

    options, args = parser.parse_args()

    encoding = options.encoding

    if args:
        if options.text:
            fatal("Can't use both FILE and -c option")
        else:
            with open(args[0], 'rb') as f:
                stream = f.read()
    elif options.text:
        if PY3:
            stream = os.fsencode(options.text)
        else:
            stream = options.text
        # add a newline to the string if it comes from the
        # command line so that the result is printed nicely
        # on the console.
        stream += '\n'.encode('ascii')
    else:
        if PY3:
            stream = sys.stdin.buffer.read()
        else:
            stream = sys.stdin.read()

    try:
        stream = stream.decode(encoding)
    except UnicodeDecodeError as e:
        fatal('Unable to decode input: %s, start: %d, end: %d' % (e.reason, e.start, e.end))

    sys.stdout.write(unidecode(stream))
