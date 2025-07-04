import datetime
import os
SAFERATES_LOG_LEVELS = {"DEBUG": 10, "INFO": 20, "SUCCESS": 25, "WARN": 30, "ERROR": 40}
SAFERATES_LOG_LEVEL = SAFERATES_LOG_LEVELS.get(os.environ.get("SAFERATES_LOG_LEVEL", "INFO").upper(), 20)
SAFERATES_LOG_FILE = os.environ.get("SAFERATES_LOG_FILE")
def saferates_log(action, details=None, level="INFO"):
    numeric = SAFERATES_LOG_LEVELS.get(level, 20)
    if numeric < SAFERATES_LOG_LEVEL:
        return
    colors = {
        "DEBUG": "\033[90m", "INFO": "\033[94m", "SUCCESS": "\033[92m",
        "WARN": "\033[93m", "ERROR": "\033[91m"
    }
    endc = "\033[0m"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{now}] [saferates] [{level}] {action}"
    if details:
        msg += f": {details}"
    print(colors.get(level, ""), msg, endc)
    if SAFERATES_LOG_FILE:
        try:
            with open(SAFERATES_LOG_FILE, "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        except Exception:
            pass