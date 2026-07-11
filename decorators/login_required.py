from functools import wraps
from utilities.logger import ApplicationLogger

def login_required(view_func: object) -> object:
    @wraps(view_func)
    def wrapper(self, *args: tuple, **kwargs: dict) -> object:
        if not hasattr(self, "current_user") or self.current_user is None:
            ApplicationLogger.warning("Login required.")
            raise PermissionError("Please login first.")
        return view_func(self, *args, **kwargs)
    return wrapper