from functools import wraps
from models.user import User

def admin_only(view_func: object) -> object:
    @wraps(view_func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, "current_user") or self.current_user is None:
            raise PermissionError("Please login first.")
        if self.current_user.role != User.ADMIN:
            raise PermissionError("Administrator access required.")
        return view_func(self, *args, **kwargs)
    return wrapper

# AuthService: use @admin_only instead of _require_admin