import Queue

from parallel import worker


class Runner(object):
    def __init__(self, num_workers=4):
        self.in_queue = Queue.Queue()
        self.out_queue = Queue.Queue()
        self.num_workers = num_workers
        self.workers = None
        self._start_workers()

    def _start_workers(self):
        self.workers = [worker.Worker(self.in_queue, self.out_queue)
                        for i in range(self.num_workers)]

    def add_task(self, task, *args, **kwargs):
        self.in_queue.put((task, args, kwargs))

    def results(self):
        self.in_queue.join()
        return self.out_queue.queue
