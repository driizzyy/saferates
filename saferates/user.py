class SaferatesUser:
    def __init__(self, saferates_api):
        self.api = saferates_api
    def profile(self):
        return self.api.get("/users/@me")
    def settings(self):
        return self.api.get("/users/@me/settings")
    def relationships(self):
        return self.api.get("/users/@me/relationships")
    def set_status(self, status="online", afk=False):
        payload = {"status": status, "afk": afk}
        return self.api.patch("/users/@me/settings", json=payload)