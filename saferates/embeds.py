from .logger import saferates_log
class SaferatesEmbeds:
    def __init__(self, api):
        self.api = api
    def saferates_build_embed(self, title=None, description=None, color=0x5865F2, fields=None, image_url=None, footer=None):
        embed = {"type": "rich"}
        if title: embed["title"] = title
        if description: embed["description"] = description
        if color: embed["color"] = color
        if image_url: embed["image"] = {"url": image_url}
        if footer: embed["footer"] = {"text": footer}
        if fields:
            embed["fields"] = [{"name": f["name"], "value": f["value"], "inline": f.get("inline", False)} for f in fields]
        return embed
    def saferates_send_embed(self, channel_id, embed):
        saferates_log("Sending embed", f"channel={channel_id}, title={embed.get('title', '')}")
        payload = {"embed": embed}
        return self.api.post(f"/channels/{channel_id}/messages", json=payload)