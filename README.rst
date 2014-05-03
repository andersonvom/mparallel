========
parallel
========

This is a minimalist parallel task runner for python programs.

Most programming languages have full support for threads but often require a
lot of overhead work even for the simplest tasks.  This package aims to provide
an easy way to parallelize these tasks with very little effort.


Getting Started
===============

First install the package.

::

  pip install parallel

In your python modules, just import it and use it as follows:

::

  import time
  import parallel

  def some_expensive_or_waiting_task(some_param):
    # ...
    time.sleep(2)
    return some_param

  def my_method():
    runner = parallel.Runner()
    for i in range(10):
      runner.add_task(some_expensive_or_waiting_task, i)
    print runner.results()

You can see the tasks are being run in parallel from the previous code because
even though they are being started in order (0..9), the final output will
likely appear in a different order.  Also, the total waiting time will be less
than 20 seconds, which is the time it would take to serially run them.
