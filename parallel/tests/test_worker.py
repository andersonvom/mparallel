import mock
import Queue
import unittest

from parallel import worker


class TestWorker(unittest.TestCase):

    def setUp(self):
        super(TestWorker, self).setUp()
        self.in_queue = Queue.Queue()
        self.out_queue = Queue.Queue()
        self.worker = worker.Worker(self.in_queue, self.out_queue)
        self.task = mock.Mock(return_value='foobar')
        self.task_info = (self.task, (), {})

    def test_worker_has_input_queue(self):
        self.assertIsInstance(self.worker.in_queue, Queue.Queue)

    def test_worker_has_output_queue(self):
        self.assertIsInstance(self.worker.out_queue, Queue.Queue)

    @mock.patch.object(worker.Worker, 'start')
    @mock.patch.object(worker.Worker, 'setDaemon')
    def test_worker_is_daemon(self, mock_daemon, mock_start):
        worker.Worker(self.in_queue, self.out_queue)
        mock_daemon.assert_called_once_with(True)

    @mock.patch.object(worker.Worker, 'start')
    def test_worker_auto_starts(self, mock_start):
        worker.Worker(self.in_queue, self.out_queue)
        mock_start.assert_called_once_with()

    @mock.patch.object(worker.Worker, 'run_task')
    def test_worker_runs_tasks_from_in_queue(self, mock_run_task):
        self.in_queue.put(self.task_info)
        self.in_queue.join()
        mock_run_task.assert_called_once_with(self.task_info)

    def test_worker_stores_results_in_output_queue(self):
        self.in_queue.put(self.task_info)
        self.in_queue.join()
        self.assertEqual('foobar', self.out_queue.queue[0])

    def test_run_task(self):
        result = self.worker.run_task(self.task_info)
        self.assertTrue(self.task.called)
        self.assertEqual(result, 'foobar')

    def test_run_task_with_multiple_args(self):
        task_info = (self.task, (1, 2, 3), {})
        self.worker.run_task(task_info)
        self.task.assert_called_once_with(1, 2, 3)

    def test_run_task_with_kwargs(self):
        task_info = (self.task, (), {'foo': 'bar'})
        self.worker.run_task(task_info)
        self.task.assert_called_once_with(foo='bar')

    def test_run_task_returns_exceptions(self):
        exc = Exception('boom!')
        self.task.side_effect = exc
        result = self.worker.run_task(self.task_info)
        self.assertEqual(result, exc)
