import time
from typing import Any
from collections.abc import Callable
from functools import wraps
from utilities.logger import ApplicationLogger

MODEL_EXECUTION_TIMES: dict[str, float] = {}

def log_execution_time(view_func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(view_func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        print("ARGS values: ", *args, "\nKWARGS dict: ", **kwargs)
        start_time: float = time.perf_counter()
        result: object = view_func(*args, **kwargs)
        end_time: float = time.perf_counter()
        execution_time: float = end_time - start_time
        ApplicationLogger.info(f"{view_func.__name__} executed in {execution_time:.4f} seconds.")
        MODEL_EXECUTION_TIMES[view_func.__name__] = execution_time
        return result
    return wrapper