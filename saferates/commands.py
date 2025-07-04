from .logger import saferates_log
class SaferatesCommands:
    def __init__(self):
        self._commands = {}
    def saferates_add_command(self, name, handler):
        saferates_log("Registering custom command", name, level="DEBUG")
        self._commands[name] = handler
    def saferates_run_command(self, name, *args, **kwargs):
        if name in self._commands:
            saferates_log("Running custom command", name)
            return self._commands[name](*args, **kwargs)
        saferates_log("Unknown command", name, level="ERROR")
        return None
    def saferates_list_commands(self):
        return list(self._commands)