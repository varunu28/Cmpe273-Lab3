from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class HelloWorld(DatagramProtocol):

    def StartProtocol(self):
        host = "localhost"
        port = 8000

        self.transport.connect(host, port)
        message = "Hello World"
        self.transport.write(message.encode())

    def datagramReceived(self, data, host):
        print("received %r from %s" % (data.decode(), host))

reactor.listenUDP(0, HelloWorld())
reactor.run()