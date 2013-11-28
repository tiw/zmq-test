__author__ = 'ting'

import zmq

context = zmq.Context()

# Socket to talk to server
print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


index = 0
# Do 10 request, waiting each time for a response
for request in range(10):
    print "Sending request ", request, "..."
    socket.send("Hello number: %s" % index)

    # Get the reply
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
    index += 1