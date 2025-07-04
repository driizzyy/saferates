from .logger import saferates_log
class SaferatesAccount:
    def __init__(self, api):
        self.api = api
    def get_profile(self):
        saferates_log("Fetching user profile")
        return self.api.get("/users/@me")
    def change_username(self, new_username, password):
        saferates_log("Changing username", f"to {new_username}")
        payload = {"username": new_username, "password": password}
        return self.api.patch("/users/@me", json=payload)
    def change_avatar(self, image_b64):
        saferates_log("Changing avatar")
        payload = {"avatar": image_b64}
        return self.api.patch("/users/@me", json=payload)
    def set_status(self, text):
        saferates_log("Setting custom status", f"text={text}")
        payload = {"custom_status": {"text": text}}
        return self.api.patch("/users/@me/settings", json=payload)
    def get_presence(self):
        saferates_log("Fetching user settings/presence")
        return self.api.get("/users/@me/settings")