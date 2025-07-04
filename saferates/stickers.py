from .logger import saferates_log
class SaferatesStickers:
    def __init__(self, api):
        self.api = api
    def saferates_send_sticker(self, channel_id, sticker_id):
        saferates_log("Sending sticker", f"channel={channel_id}, sticker={sticker_id}")
        payload = {"sticker_ids": [sticker_id]}
        return self.api.post(f"/channels/{channel_id}/messages", json=payload)