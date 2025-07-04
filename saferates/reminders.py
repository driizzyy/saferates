from .logger import saferates_log
import threading
import time
class SaferatesReminders:
    def __init__(self, api):
        self.api = api
    def saferates_remind_me(self, user_id, content, delay_seconds):
        saferates_log("Scheduling reminder", f"user={user_id}, delay={delay_seconds}")
        def delayed_send():
            time.sleep(delay_seconds)
            self.api.post("/users/@me/channels", json={"recipients": [user_id]})
            dms = self.api.get("/users/@me/channels")
            dm_id = None
            for dm in dms:
                if any(r["id"] == user_id for r in dm.get("recipients", [])):
                    dm_id = dm["id"]
                    break
            if dm_id:
                self.api.post(f"/channels/{dm_id}/messages", json={"content": content})
        thread = threading.Thread(target=delayed_send)
        thread.start()
        return "Reminder scheduled."