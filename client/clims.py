import requests
from optparse import OptionParser


def Main(options):
    return "options"

if __name__ == '__main__':
    usage = "usage: %prog [options] <title> <text>"
    parser = OptionParser(usage=usage)
    parser.add_option("-l", "--long",
                      help="Long post")
    parser.add_option("-s", "--short",
                      help="Short post")

    (options, args) = parser.parse_args()
    Main(options)