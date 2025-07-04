from .logger import saferates_log
import httpx
class SaferatesWebhooks:
    def send(self, webhook_url, content, username=None, avatar_url=None, embeds=None):
        saferates_log("Sending webhook", f"url={webhook_url}, content={content[:40]}")
        payload = {"content": content}
        if username:
            payload["username"] = username
        if avatar_url:
            payload["avatar_url"] = avatar_url
        if embeds:
            payload["embeds"] = embeds
        resp = httpx.post(webhook_url, json=payload)
        saferates_log("Webhook sent", level="SUCCESS")
        return resp.json()
    def edit(self, webhook_url, message_id, content=None, embeds=None):
        saferates_log("Editing webhook message", f"url={webhook_url}, id={message_id}")
        payload = {}
        if content:
            payload["content"] = content
        if embeds:
            payload["embeds"] = embeds
        url = f"{webhook_url}/messages/{message_id}"
        resp = httpx.patch(url, json=payload)
        saferates_log("Webhook edited", level="SUCCESS")
        return resp.json()
    def delete(self, webhook_url, message_id):
        saferates_log("Deleting webhook message", f"url={webhook_url}, id={message_id}")
        url = f"{webhook_url}/messages/{message_id}"
        resp = httpx.delete(url)
        saferates_log("Webhook deleted", level="SUCCESS")
        return resp.status_code == 204