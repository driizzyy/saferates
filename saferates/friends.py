from .logger import saferates_log
class SaferatesFriends:
    def __init__(self, api):
        self.api = api
    def add(self, user_id):
        saferates_log("Adding friend", f"user_id={user_id}")
        return self.api.put(f"/users/@me/relationships/{user_id}", json={"type": 1})
    def remove(self, user_id):
        saferates_log("Removing friend", f"user_id={user_id}")
        return self.api.delete(f"/users/@me/relationships/{user_id}")
    def block(self, user_id):
        saferates_log("Blocking user", f"user_id={user_id}")
        return self.api.put(f"/users/@me/relationships/{user_id}", json={"type": 2})
    def unblock(self, user_id):
        saferates_log("Unblocking user", f"user_id={user_id}")
        return self.api.delete(f"/users/@me/relationships/{user_id}")
    def get_relationships(self):
        saferates_log("Fetching relationships/friends list")
        return self.api.get("/users/@me/relationships")