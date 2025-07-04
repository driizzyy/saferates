from .logger import saferates_log
class SaferatesModerator:
    def __init__(self, api):
        self.api = api
    def saferates_kick(self, guild_id, user_id):
        saferates_log("Kicking user", f"guild={guild_id}, user={user_id}")
        return self.api.delete(f"/guilds/{guild_id}/members/{user_id}")
    def saferates_ban(self, guild_id, user_id, delete_message_days=0, reason=None):
        saferates_log("Banning user", f"guild={guild_id}, user={user_id}")
        params = {"delete_message_days": delete_message_days}
        if reason: params["reason"] = reason
        return self.api.put(f"/guilds/{guild_id}/bans/{user_id}", params=params)
    def saferates_unban(self, guild_id, user_id):
        saferates_log("Unbanning user", f"guild={guild_id}, user={user_id}")
        return self.api.delete(f"/guilds/{guild_id}/bans/{user_id}")
    def saferates_timeout(self, guild_id, user_id, until_iso8601):
        saferates_log("Timing out user", f"guild={guild_id}, user={user_id}, until={until_iso8601}")
        payload = {"communication_disabled_until": until_iso8601}
        return self.api.patch(f"/guilds/{guild_id}/members/{user_id}", json=payload)