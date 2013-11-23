# -*- coding: utf-8 -*-
import socks
import socket
import shell
import sys

if __name__ == '__main__':
    # подключаемся к Tor
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)
    socket.socket = socks.socksocket
    shell.main(sys.argv[1], sys.argv[2])