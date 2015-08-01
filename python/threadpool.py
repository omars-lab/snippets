import time
import unittest

from multiprocessing.dummy import Pool as ThreadPool


class Tester(unittest.TestCase):
    def test_async(self):
        """
        Runs 1000 threads each that sleep for 1 second. Since we are
        running 100 threads at a time, everything should take about 10 seconds,
        give or take 5 seconds (gut feeling)
        """
        start = int(time.time())

        threads = []

        def thread(id):
            time.sleep(1)
            threads.append("Thread-{} Done".format(id))

        # Thread pool of 100 threads
        pool = ThreadPool(100)
        pool.map(thread, range(0, 1000))
        pool.close()
        pool.join()

        now = time.time()

        self.assertEquals(now-start < 15, True)

if __name__ == "__main__":
    unittest.main()
