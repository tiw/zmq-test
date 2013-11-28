__author__ = 'ting'

import zmq
from time import sleep

context = zmq.Context()
responder = context.socket(zmq.REP)
responder.bind("tcp://*:5555")

index = 1

while True:
    request = responder.recv()
    print "Received request: %s" % request
    sleep(1)
    responder.send("%s world %i" % (request, index))
    index += 1
