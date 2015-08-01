# Justification
	Accept a set of file descriptors you are interested in performing I/O with.
	Tell you, repeatedly, when any file descriptors are ready for I/O.

# Proper Implementations
  * Handle all the weird corner cases that crop up on different systems.
  * Provide lots of nice abstractions to help you use the reactor with the least amount of effort.
  * Provide implementations of public protocols that you can use out of the box.

# Notes
During a callback, the Twisted loop is effectively “blocked” on our code.
So we should make sure our callback code doesn’t waste any time.
In particular, we should avoid making blocking I/O calls in our callbacks.
Otherwise, we would be defeating the whole point of using the reactor pattern
in the first place. Twisted will not take any special precautions to prevent
our code from blocking, we just have to make sure not to do it. As we will
eventually see, for the common case of network I/O we don’t have to worry
about it as we let Twisted do the asynchronous communication for us.

Other examples of potentially blocking operations include reading or writing
from a non-socket file descriptor (like a pipe) or waiting for a subprocess to
finish. Exactly how you switch from blocking to non-blocking operations is
specific to what you are doing, but there is often a Twisted API that will help
you do it. Note that many standard Python functions have no way to switch to a
non-blocking mode. For example, the os.system function will always block until
the subprocess is finished. That’s just how it works. So when using Twisted,
you will have to eschew os.system in favor of the Twisted API for launching
subprocesses.
