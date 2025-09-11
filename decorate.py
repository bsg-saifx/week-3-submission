import functools
import time
import requests

def retry(times=3, delay=0, increase_delay=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[{func.__name__}] try {attempts} failed: {e}")
                    if attempts == times:
                        raise 
                    if current_delay:
                        print(f"Retry in {current_delay} seconds")
                        time.sleep(current_delay)
                        if increase_delay:
                            current_delay *= 2
        return wrapper
    return decorator

@retry(times=3, delay=1, increase_delay=True)
def fetch_json():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=3)
    response.raise_for_status() 
    return response.json()

if __name__ == "__main__":
    try:
        json = fetch_json()
        print(f"Fetched {len(json)} items.")
    except Exception as e:
        print(f"Failed: {e}")


