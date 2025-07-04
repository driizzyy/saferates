from .logger import saferates_log
class SaferatesAudit:
    def __init__(self, api):
        self.api = api
    def saferates_get_audit_logs(self, guild_id, limit=50, action_type=None, user_id=None):
        saferates_log("Fetching audit logs", f"guild={guild_id}")
        params = {"limit": limit}
        if action_type: params["action_type"] = action_type
        if user_id: params["user_id"] = user_id
        return self.api.get(f"/guilds/{guild_id}/audit-logs", params=params)