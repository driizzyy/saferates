from .logger import saferates_log
class SaferatesWelcome:
    def __init__(self, api):
        self.api = api
    def saferates_welcome_new_friend(self, user_id, message):
        saferates_log("Welcoming new friend", f"user={user_id}")
        payload = {"recipients": [user_id]}
        dm = self.api.post("/users/@me/channels", json=payload)
        dm_id = dm.get("id")
        if dm_id:
            return self.api.post(f"/channels/{dm_id}/messages", json={"content": message})
        return None