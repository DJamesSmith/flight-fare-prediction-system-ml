import time
from functools import wraps
from utilities.logger import ApplicationLogger

MODEL_EXECUTION_TIMES: dict[str, float] = {}

def log_execution_time(view_func: object) -> object:
    @wraps(view_func)
    def wrapper(*args: tuple, **kwargs: dict) -> object:
        print("ARGS values: ", *args, "\nKWARGS dict: ", **kwargs)
        start_time: float = time.perf_counter()
        result: object = view_func(*args, **kwargs)
        end_time: float = time.perf_counter()
        execution_time = end_time - start_time
        # elapsed_time: float = round(end_time - start_time, 4)
        ApplicationLogger.info(f"{function.__name__} executed in {execution_time:.4f} seconds.")
        MODEL_EXECUTION_TIMES[view_func.__name__] = execution_time
        # MODEL_EXECUTION_TIMES[view_func.__name__] = elapsed_time
        return result
    return wrapper