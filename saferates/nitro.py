from .logger import saferates_log
class SaferatesNitro:
    def __init__(self, api):
        self.api = api
    def saferates_check_nitro(self):
        saferates_log("Checking Nitro status")
        profile = self.api.get("/users/@me")
        premium = profile.get("premium_type", 0)
        perks = {
            0: "None",
            1: "Nitro Classic",
            2: "Nitro",
            3: "Nitro Basic"
        }
        return {"type": premium, "perks": perks.get(premium, "Unknown")}
    def saferates_set_animated_avatar(self, image_b64):
        saferates_log("Setting animated avatar")
        payload = {"avatar": image_b64}
        return self.api.patch("/users/@me", json=payload)