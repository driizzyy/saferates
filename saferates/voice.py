from .logger import saferates_log
class SaferatesVoice:
    def __init__(self, api):
        self.api = api
    def saferates_move_to_voice(self, guild_id, channel_id):
        saferates_log("Moving self to voice", f"guild={guild_id}, channel={channel_id}")
        payload = {"channel_id": channel_id}
        return self.api.patch(f"/guilds/{guild_id}/members/@me", json=payload)
    def saferates_disconnect_voice(self, guild_id):
        saferates_log("Disconnecting from voice", f"guild={guild_id}")
        payload = {"channel_id": None}
        return self.api.patch(f"/guilds/{guild_id}/members/@me", json=payload)