from .logger import saferates_log
class SaferatesDMs:
    def __init__(self, api):
        self.api = api
    def list_dm_channels(self):
        saferates_log("Fetching DM channels")
        return self.api.get("/users/@me/channels")
    def create_dm(self, recipient_id):
        saferates_log("Creating DM channel", f"recipient={recipient_id}")
        payload = {"recipients": [recipient_id]}
        return self.api.post("/users/@me/channels", json=payload)
    def send_dm(self, user_id, content):
        saferates_log("Sending DM", f"user_id={user_id}, content={content[:40]}")
        dm = self.create_dm(user_id)
        dm_channel_id = dm.get("id") if isinstance(dm, dict) else None
        if not dm_channel_id:
            saferates_log("Failed to create DM", f"user_id={user_id}", level="ERROR")
            return None
        return self.api.post(f"/channels/{dm_channel_id}/messages", json={"content": content})
    def delete_dm_channel(self, channel_id):
        saferates_log("Deleting DM channel", f"channel_id={channel_id}")
        return self.api.delete(f"/channels/{channel_id}")
    def bulk_dm(self, user_ids, content):
        results = []
        for user_id in user_ids:
            res = self.send_dm(user_id, content)
            results.append(res)
        return results