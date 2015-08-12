from twisted.internet import reactor, defer

d = defer.Deferred()
# What happends if we run the following line:
# d.addCallback(test)

reactor.callLater(100, reactor.stop)
reactor.callLater(2, d.callback, 5)
reactor.run()


@defer.inlineCallbacks
def test():
    x = yield d
    print x

test()
