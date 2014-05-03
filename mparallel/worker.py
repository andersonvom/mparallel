import threading


class Worker(threading.Thread):

    def __init__(self, in_queue, out_queue):
        super(Worker, self).__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.setDaemon(True)
        self.start()

    def run_task(self, task_info):
        try:
            task, args, kwargs = task_info
            return task(*args, **kwargs)
        except Exception as exc:
            return exc

    def run(self):
        while True:
            task_info = self.in_queue.get()
            result = self.run_task(task_info)
            self.out_queue.put(result)
            self.in_queue.task_done()
