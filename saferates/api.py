import httpx
import asyncio
class SaferatesTokenError(Exception):
    pass
class SaferatesAPI:
    BASE_URL = "https://discord.com/api/v10"
    def __init__(self, user_token: str):
        if not user_token or user_token.startswith("Bot "):
            raise SaferatesTokenError("SaferatesAPI only accepts user tokens, not bot tokens.")
        self.user_token = user_token
    async def _request_async(self, method, endpoint, **kwargs):
        headers = kwargs.pop('headers', {})
        headers['Authorization'] = self.user_token
        url = endpoint if endpoint.startswith("http") else f"{self.BASE_URL}{endpoint}"
        async with httpx.AsyncClient() as client:
            resp = await client.request(method, url, headers=headers, **kwargs)
            resp.raise_for_status()
            try:
                return resp.json()
            except Exception:
                return resp.text
    def _request(self, method, endpoint, **kwargs):
        return asyncio.run(self._request_async(method, endpoint, **kwargs))
    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)
    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)
    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)
    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)