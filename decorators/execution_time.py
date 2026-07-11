import time
from functools import wraps
MODEL_EXECUTION_TIMES: dict[str, float] = {}

def log_execution_time(view_func: object) -> object:
    @wraps(view_func)
    def wrapper(*args: tuple, **kwargs: dict) -> object:
        start_time: float = time.perf_counter()
        result: object = view_func(*args, **kwargs)
        end_time: float = time.perf_counter()
        elapsed_time: float = round(end_time - start_time, 4)
        MODEL_EXECUTION_TIMES[view_func.__name__] = elapsed_time
        return result
    return wrapper