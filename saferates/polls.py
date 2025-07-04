from .logger import saferates_log
class SaferatesPolls:
    def __init__(self, api):
        self.api = api
    def saferates_create_poll(self, channel_id, question, options):
        saferates_log("Creating poll", f"channel={channel_id}, question={question}")
        message = self.api.post(f"/channels/{channel_id}/messages", json={"content": question + "\n" + "\n".join(options)})
        msg_id = message.get("id")
        for emoji in options:
            self.api.put(f"/channels/{channel_id}/messages/{msg_id}/reactions/{emoji}/@me")
        return message