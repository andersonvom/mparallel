import multiprocessing


try:
    NUM_WORKERS = multiprocessing.cpu_count()
except NotImplementedError:
    NUM_WORKERS = 4
