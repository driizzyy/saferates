from .logger import saferates_log
class SaferatesGuilds:
    def __init__(self, api):
        self.api = api
    def list(self):
        saferates_log("Fetching guilds list")
        return self.api.get("/users/@me/guilds")
    def leave(self, guild_id):
        saferates_log("Leaving guild", f"guild_id={guild_id}")
        return self.api.delete(f"/users/@me/guilds/{guild_id}")
    def join_by_invite(self, invite_code):
        saferates_log("Joining guild via invite", f"invite={invite_code}")
        return self.api.post(f"/invites/{invite_code}")
    def is_boosting(self, guild_id):
        saferates_log("Checking if boosting server", f"guild_id={guild_id}")
        guild_info = self.api.get(f"/users/@me/guilds")
        for guild in guild_info:
            if guild.get("id") == guild_id and guild.get("premium_since"):
                return True
        return False
    def mass_leave(self, guild_ids):
        results = []
        for gid in guild_ids:
            res = self.leave(gid)
            results.append(res)
        return results