from functools import wraps
from utilities.logger import ApplicationLogger

def exception_handler(view_func: object) -> object:
    @wraps(view_func)
    def wrapper(self, *args: tuple, **kwargs: dict) -> object:
        try:
            return view_func(*args, **kwargs)
        except Exception as error:
            ApplicationLogger.error(str(error))
            print(error)
    return wrapper


# NOT to be used in Service layers since there's already custom exception handling there.