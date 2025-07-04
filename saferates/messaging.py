from .logger import saferates_log
class SaferatesMessaging:
    def __init__(self, api):
        self.api = api
    def send_message(self, channel_id, content, embed=None):
        saferates_log("Sending message", f"channel={channel_id}, content={content[:40]}")
        payload = {"content": content}
        if embed:
            payload["embed"] = embed
        result = self.api.post(f"/channels/{channel_id}/messages", json=payload)
        saferates_log("Message sent", f"channel={channel_id}, response={str(result)[:60]}", level="SUCCESS")
        return result
    def send_embed(self, channel_id, embed_dict):
        saferates_log("Sending embed", f"channel={channel_id}")
        payload = {"embed": embed_dict}
        return self.api.post(f"/channels/{channel_id}/messages", json=payload)
    def send_attachment(self, channel_id, filepath, content=None):
        saferates_log("Uploading attachment", f"channel={channel_id}, file={filepath}")
        with open(filepath, "rb") as f:
            files = {"file": (filepath, f)}
            data = {"content": content or ""}
            return self.api.post(f"/channels/{channel_id}/messages", files=files, data=data)
    def edit_message(self, channel_id, message_id, new_content):
        saferates_log("Editing message", f"channel={channel_id}, msg_id={message_id}")
        payload = {"content": new_content}
        return self.api.patch(f"/channels/{channel_id}/messages/{message_id}", json=payload)
    def delete_message(self, channel_id, message_id):
        saferates_log("Deleting message", f"channel={channel_id}, msg_id={message_id}")
        return self.api.delete(f"/channels/{channel_id}/messages/{message_id}")
    def bulk_delete(self, channel_id, message_ids):
        saferates_log("Bulk deleting messages", f"channel={channel_id}, ids={message_ids}")
        payload = {"messages": message_ids}
        return self.api.post(f"/channels/{channel_id}/messages/bulk-delete", json=payload)
    def crosspost_message(self, channel_id, message_id):
        saferates_log("Crossposting message", f"channel={channel_id}, msg_id={message_id}")
        return self.api.post(f"/channels/{channel_id}/messages/{message_id}/crosspost")
    def pin_message(self, channel_id, message_id):
        saferates_log("Pinning message", f"channel={channel_id}, msg_id={message_id}")
        return self.api.put(f"/channels/{channel_id}/pins/{message_id}")
    def unpin_message(self, channel_id, message_id):
        saferates_log("Unpinning message", f"channel={channel_id}, msg_id={message_id}")
        return self.api.delete(f"/channels/{channel_id}/pins/{message_id}")
    def send_webhook(self, webhook_url, content, username=None):
        saferates_log("Sending webhook message", f"url={webhook_url}")
        payload = {"content": content}
        if username:
            payload["username"] = username
        import httpx
        resp = httpx.post(webhook_url, json=payload)
        return resp.json()