#!/usr/bin/env python

import tftpy

server = tftpy.TftpServer('.')
server.listen('127.0.0.1', 4444)
