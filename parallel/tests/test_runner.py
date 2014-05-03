import mock
import unittest

from parallel import runner


class TestRunner(unittest.TestCase):

    def setUp(self):
        super(TestRunner, self).setUp()
        self.runner = runner.Runner()

    def test_runner_has_input_output_queue(self):
        self.assertIsInstance(self.runner.in_queue, runner.Queue.Queue)
        self.assertIsInstance(self.runner.out_queue, runner.Queue.Queue)

    def test_runner_auto_start_workers(self):
        self.assertNotEqual(0, len(self.runner.workers))
        for w in self.runner.workers:
            self.assertIsInstance(w, runner.worker.Worker)

    def test_add_task(self):
        task = mock.Mock(return_value='foobar')
        with mock.patch.object(self.runner.in_queue, 'put') as mock_put:
            self.runner.add_task(task)
            mock_put.assert_called_once_with((task, (), {}))

    def test_add_task_with_multiple_args(self):
        task = mock.Mock(return_value='foobar')
        with mock.patch.object(self.runner.in_queue, 'put') as mock_put:
            self.runner.add_task(task, 1, 2)
            mock_put.assert_called_once_with((task, (1, 2), {}))

    def test_add_task_with_kwargs(self):
        task = mock.Mock(return_value='foobar')
        with mock.patch.object(self.runner.in_queue, 'put') as mock_put:
            self.runner.add_task(task, foo='bar')
            mock_put.assert_called_once_with((task, (), {'foo': 'bar'}))

    def test_results(self):
        self.runner.add_task(mock.Mock(return_value='foo'))
        self.runner.add_task(mock.Mock(return_value='bar'))
        self.runner.add_task(mock.Mock(return_value='baz'))

        results = self.runner.results()
        self.assertIn('foo', results)
        self.assertIn('bar', results)
        self.assertIn('baz', results)
