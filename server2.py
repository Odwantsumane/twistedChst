from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Server(Protocol):

    def __init__(self, users):
        self.users = users
        self.name = "unknown"

    def connectionMade(self):
        print("New connection")
        
        self.users.append(self)
        # self.transport.write(("Hello from the server").encode("utf-8"))

    def dataReceived(self, data):
        if self.name == "unknown":
            self.name = data
            print("User's name is " + self.name.decode("utf-8"))

        else:
            for user in self.users:
                if user != self:
                    user.transport.write(("<"+self.name.decode("utf-8")+"> ").encode("utf-8"))
                    user.transport.write(data)

class serverFactory(ServerFactory):

    def __init__(self):
        self.users = []

    def buildProtocol(self, addr):
        return Server(self.users)

if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(serverFactory())
    reactor.run()
