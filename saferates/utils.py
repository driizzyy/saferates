import urllib.parse
import json
import base64
def saferates_encode_emoji(emoji):
    if emoji.startswith("<:") or emoji.startswith("<a:"):
        parts = emoji.strip("<>").split(":")
        if len(parts) == 3:
            name, eid = parts[1], parts[2]
            return f"{name}:{eid}"
    return urllib.parse.quote(emoji)
def saferates_pretty_json(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)
def saferates_image_to_base64(filepath):
    with open(filepath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    ext = filepath.split(".")[-1].lower()
    return f"data:image/{ext};base64,{b64}"