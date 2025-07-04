from .logger import saferates_log
from .utils import saferates_encode_emoji
class SaferatesReactions:
    def __init__(self, api):
        self.api = api
    def react(self, channel_id, message_id, emoji):
        saferates_log("Reacting to message", f"channel={channel_id}, msg_id={message_id}, emoji={emoji}")
        emoji_enc = saferates_encode_emoji(emoji)
        return self.api.put(f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_enc}/@me")
    def unreact(self, channel_id, message_id, emoji):
        saferates_log("Removing reaction", f"channel={channel_id}, msg_id={message_id}, emoji={emoji}")
        emoji_enc = saferates_encode_emoji(emoji)
        return self.api.delete(f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_enc}/@me")