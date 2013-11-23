# -*- coding: utf-8 -*-
import sys
import urllib

class Shell(object):
    def __init__(self, url, encoding, **kwargs):
        self.url = url
        self.encoding = encoding

    def eval(self, s):
        res = urllib.urlopen(self.url, 'eval=' + urllib.quote(s.encode(self.encoding)))
        return res.read().decode(self.encoding)

def main(url, encoding):
    shell = Shell(url, encoding)
    print("""Python Remote Shell ver 0.1
Copyright 2013 tz4678@gmail.com""")
    while True:
        v = raw_input('shell> ').decode(sys.stdin.encoding)
        try:
            print('output: ' + shell.eval(v))
        except Exception, e:
            print('An exception was caught: {}'.format(e))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])