from .utils import saferates_encode_emoji, saferates_send_typing, saferates_upload_file
class SaferatesChannels:
    def __init__(self, saferates_api):
        self.api = saferates_api
    def info(self, channel_id):
        return self.api.get(f"/channels/{channel_id}")
    def send_message(self, channel_id, content, embed=None, tts=False):
        data = {"content": content, "tts": tts}
        if embed:
            data["embed"] = embed
        return self.api.post(f"/channels/{channel_id}/messages", json=data)
    def send_file(self, channel_id, file_path, content=None):
        return saferates_upload_file(self.api, channel_id, file_path, content)
    def delete_message(self, channel_id, message_id):
        return self.api.delete(f"/channels/{channel_id}/messages/{message_id}")
    def edit_message(self, channel_id, message_id, new_content):
        return self.api.patch(f"/channels/{channel_id}/messages/{message_id}", json={"content": new_content})
    def react(self, channel_id, message_id, emoji):
        emoji_enc = saferates_encode_emoji(emoji)
        return self.api.put(f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_enc}/@me")
    def unreact(self, channel_id, message_id, emoji):
        emoji_enc = saferates_encode_emoji(emoji)
        return self.api.delete(f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_enc}/@me")
    def dm_channels(self):
        return self.api.get("/users/@me/channels")
    def create_dm(self, recipient_id):
        return self.api.post("/users/@me/channels", json={"recipients": [recipient_id]})
    def send_dm(self, user_id, content):
        dm = self.create_dm(user_id)
        dm_channel_id = dm.get("id") if isinstance(dm, dict) else None
        if not dm_channel_id:
            return None
        return self.send_message(dm_channel_id, content)
    def typing(self, channel_id):
        return saferates_send_typing(self.api, channel_id)