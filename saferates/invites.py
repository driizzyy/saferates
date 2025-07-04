from .logger import saferates_log
class SaferatesInvites:
    def __init__(self, api):
        self.api = api
    def saferates_create_invite(self, channel_id, max_age=86400, max_uses=1, temporary=False, unique=True):
        saferates_log("Creating invite", f"channel_id={channel_id}")
        payload = {
            "max_age": max_age, "max_uses": max_uses,
            "temporary": temporary, "unique": unique
        }
        return self.api.post(f"/channels/{channel_id}/invites", json=payload)
    def saferates_delete_invite(self, invite_code):
        saferates_log("Revoking invite", f"code={invite_code}")
        return self.api.delete(f"/invites/{invite_code}")