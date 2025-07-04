from .logger import saferates_log
import json
class SaferatesBackup:
    def __init__(self, api):
        self.api = api
    def saferates_backup_guild(self, guild_id, path=None):
        saferates_log("Backing up guild", f"guild_id={guild_id}")
        info = self.api.get(f"/guilds/{guild_id}")
        members = self.api.get(f"/guilds/{guild_id}/members", params={"limit": 1000})
        data = {"info": info, "members": members}
        if not path:
            path = f"guild_{guild_id}_backup.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return path