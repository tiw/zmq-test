# -*- coding: utf-8 -*-
__author__ = 'wangting'


""" generate log for the subscriber
"""

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")


message = ' '.join(sys.argv[1:]) or "Hello World!"
while 1:
    zipcode = 'info'
    socket.send("%s %s" % ('info', message))
