from .logger import saferates_log
class SaferatesEmojis:
    def __init__(self, api):
        self.api = api
    def saferates_list_emojis(self, guild_id):
        saferates_log("Listing emojis", f"guild={guild_id}")
        return self.api.get(f"/guilds/{guild_id}/emojis")
    def saferates_get_emoji(self, guild_id, emoji_id):
        saferates_log("Fetching emoji", f"guild={guild_id}, emoji={emoji_id}")
        return self.api.get(f"/guilds/{guild_id}/emojis/{emoji_id}")
    def saferates_upload_emoji(self, guild_id, name, image_b64, roles=None):
        saferates_log("Uploading emoji", f"guild={guild_id}, name={name}")
        payload = {"name": name, "image": image_b64}
        if roles: payload["roles"] = roles
        return self.api.post(f"/guilds/{guild_id}/emojis", json=payload)
    def saferates_delete_emoji(self, guild_id, emoji_id):
        saferates_log("Deleting emoji", f"guild={guild_id}, emoji={emoji_id}")
        return self.api.delete(f"/guilds/{guild_id}/emojis/{emoji_id}")