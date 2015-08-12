"""
Still Broken
"""

import time
import threading
import StringIO

TASKS = []


def task(_time, out):
    for i in range(_time):
        out.write('thinking')
        time.sleep(1)


def call_task(func, param):
    o = StringIO.StringIO()
    t = threading.Thread(target=func, args=(param, o))
    t.start()
    TASKS.append((t, o))

for i in range(10, 120, 5):
    call_task(task, i)

for task, output in TASKS:
    task.join()
    output.seek(0)
    print output.read()
