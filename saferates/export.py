from .logger import saferates_log
import json
class SaferatesExport:
    def __init__(self, api):
        self.api = api
    def saferates_export_friends(self, path="friends_backup.json"):
        saferates_log("Exporting friends list", f"to {path}")
        friends = self.api.get("/users/@me/relationships")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(friends, f, indent=2, ensure_ascii=False)
        return path