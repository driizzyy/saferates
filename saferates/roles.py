from .logger import saferates_log
class SaferatesRoles:
    def __init__(self, api):
        self.api = api
    def saferates_add_self_role(self, guild_id, user_id, role_id):
        saferates_log("Adding self role", f"guild={guild_id}, role={role_id}")
        return self.api.put(f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}")
    def saferates_remove_self_role(self, guild_id, user_id, role_id):
        saferates_log("Removing self role", f"guild={guild_id}, role={role_id}")
        return self.api.delete(f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}")