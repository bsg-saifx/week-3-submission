import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter() 
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()  
        self.interval = self.end - self.start
        print(f"Elapsed time: {self.interval:.6f} seconds")

with Timer() as t:
    for _ in range(1000000):
        pass

