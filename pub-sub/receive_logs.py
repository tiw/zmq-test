# -*- coding: utf-8 -*-
__author__ = 'wangting'

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")
log_filter = 'info'
# NOTE: for the sub-pub pattern zmq.SUBSCRIBE is obligate
socket.setsockopt(zmq.SUBSCRIBE, log_filter)

string = socket.recv()
print " [x] %r" % (string,)
