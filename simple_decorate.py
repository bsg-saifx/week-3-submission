import functools

def simple_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                if attempt < 2:
                    raise Exception("Simulated failure")
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == 2:  
                    raise
    return wrapper

@simple_decorator
def basefucntion(food):
    print(f"Inside the base function there is {food}")   

if __name__ == "__main__":
    basefucntion("Ice Cream")

