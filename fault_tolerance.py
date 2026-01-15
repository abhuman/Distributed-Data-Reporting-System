import time
import functools

def retry(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise Exception("All retries failed")
        return wrapper
    return decorator
