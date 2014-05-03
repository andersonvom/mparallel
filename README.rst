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

  import parallel


  def some_expensive_or_waiting_task(*args, **kwargs):
    import time
    import random

    time.sleep(random.randint(0, 5))
    return args, kwargs


  def my_method():
    runner = parallel.Runner()
    for i in range(10):
      runner.add_task(some_expensive_or_waiting_task, i)
    print runner.results()
