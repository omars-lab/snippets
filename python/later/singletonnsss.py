"""
Still Broken
"""

import threading, socket, select

# Based on tornado.ioloop.IOLoop.instance() approach.
# # See https://github.com/facebook/tornado
# class SingletonMixin(object):
#     __singleton_lock = threading.Lock()
#     __singleton_instance = None

#     @classmethod
#     def instance(cls):
#         if not cls.__singleton_instance:
#             with cls.__singleton_lock:
#                 if not cls.__singleton_instance:
#                     cls.__singleton_instance = cls()
#         return cls.__singleton_instance



class Singleton(object):
  _singleton_lock = threading.Lock()
  _instance = None
  def __new__(class_, *args, **kwargs):
    with class_._singleton_lock:
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance


class _Reader(Singleton):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(0)
        self.socket.bind(("127.0.0.1", 80))
        self.socket.listen(1)

reader = _Reader().socket

writer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writer.setblocking(0)
writer.connect(("127.0.0.1", 80))
writer.send("1")

inputs = [reader]

try:
  while 1:
    r,_,_ = select.select(inputs,[],[], 0)
    for s in r:
      if s is reader:
        # A "readable" server socket is ready to accept a connection
        connection, client_address = s.accept()
        connection.setblocking(0)
        inputs.append(connection)
      else:
        data = s.recv(1)
        if data:
          writer.send("1")

except Exception as e:
  print e
