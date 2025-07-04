from .logger import saferates_log
class SaferatesAntiSpam:
    def __init__(self, api):
        self.api = api
    def saferates_block_nonfriend_dms(self):
        saferates_log("Pruning DMs from non-friends")
        channels = self.api.get("/users/@me/channels")
        friends = self.api.get("/users/@me/relationships")
        friend_ids = {f["id"] for f in friends if f["type"] == 1}
        results = []
        for dm in channels:
            recipients = [u["id"] for u in dm.get("recipients", [])]
            if not any(uid in friend_ids for uid in recipients):
                res = self.api.delete(f"/channels/{dm['id']}")
                results.append({"channel_id": dm["id"], "result": res})
        return results