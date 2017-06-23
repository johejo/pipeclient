import socket
import sys
from urllib.parse import urlparse


def main():
    argv = sys.argv
    argc = len(argv)

    port = 80

    n = 5

    #set domain and filepath
    url = urlparse(argv[1])
    # print(url)
    # print(url.netloc)

    address = (socket.gethostbyname(url.netloc), port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)
    msg = set_message(url)


def set_message(url):

    msg = 'GET {0} HTTP1.1\r\nHost: {1}\r\nRange: byte={2}-{3}\r\n\r\n'.format(url.)

    return msg


if __name__ == '__main__':
    main()
