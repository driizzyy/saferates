from .logger import saferates_log
class SaferatesHistory:
    def __init__(self, api):
        self.api = api
    def saferates_get_history(self, channel_id, limit=100, before=None, after=None):
        saferates_log("Fetching channel history", f"channel_id={channel_id}, limit={limit}")
        params = {"limit": limit}
        if before: params["before"] = before
        if after: params["after"] = after
        return self.api.get(f"/channels/{channel_id}/messages", params=params)