import aiohttp

class BadInput:
    def __init__(self, msg="Bad Input"):
        super().__init__(msg)

class NonManner:
    def __init__(self):
        self.url = "https://userdb.ourmc.space/api/v1/report"

    async def search_by_name(self, username: str, skip=0, limit=100):
        return await self.__aiohttp_request("search", username, skip, limit)

    async def get_all(self, skip=0, limit=100):
        return await self.__aiohttp_request("all", "nobody", skip, limit)

    async def get_count(self, uuid: str):
        return await self.__aiohttp_request("reportcount", uuid)

    async def get_user(self, uuid: str):
        return await self.__aiohttp_request("user", uuid)

    async def __aiohttp_request(self, point: str, user: str, skip=0, limit=100):
        params = {"skip": skip, "limit": limit}
        if point not in ["reportcount", "user", "all", "search"]:
            raise BadInput("Cannot find endpoint that named {point}")

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}/{point}/{user}", param=param) as result:
                return await result.json(content_type=None)
