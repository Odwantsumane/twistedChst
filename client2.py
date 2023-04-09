from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint

class client(Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)

    def dataReceived(self, data):
        data = data.decode("utf-8")
        print(data)

    def send_data(self):
        self.transport.write(input("Enter your name: ").encode("utf-8"))
        while True:
            self.transport.write(input().encode("utf-8"))

class clientFactory(ClientFactory):


    def buildProtocol(self, addr):
        return client()
    
if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 2000)
    endpoint.connect(clientFactory())
    reactor.run()