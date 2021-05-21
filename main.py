import aiohttp


class NonManner():
    def __init__(self):
        self.url = "https://userdb.ourmc.space/api/v1"

    async def search_by_name(self, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/report/search/{username}") as result:
                response = await result.json(content_type=None)
                rs = response["value"]
                if rs["count"] is 0:
                    return {"result": False}
                else:
                    return {"result": True, "reason": rs["list"][0]["specificReason"]}
