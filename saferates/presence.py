from .logger import saferates_log
class SaferatesPresence:
    def __init__(self, api):
        self.api = api
    def saferates_set_custom_status(self, text):
        saferates_log("Setting custom status", text)
        payload = {"custom_status": {"text": text}}
        return self.api.patch("/users/@me/settings", json=payload)
    def saferates_set_presence(self, status="online", activity_name=None, activity_type=0):
        saferates_log("Setting presence", f"status={status}, activity={activity_name}")
        data = {"status": status}
        if activity_name:
            data["game"] = {"name": activity_name, "type": activity_type}
        return self.api.patch("/users/@me/settings", json=data)