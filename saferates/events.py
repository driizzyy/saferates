from .logger import saferates_log
class SaferatesEventSystem:
    def __init__(self):
        self._handlers = {}
    def on(self, event_name):
        def decorator(func):
            self._handlers.setdefault(event_name, []).append(func)
            saferates_log("Registered event handler", event_name, level="DEBUG")
            return func
        return decorator
    def dispatch(self, event_name, *args, **kwargs):
        for func in self._handlers.get(event_name, []):
            saferates_log("Dispatching event", event_name, level="DEBUG")
            func(*args, **kwargs)