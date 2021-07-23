from io import BytesIO

import aiohttp


class SnowClient:
    def __init__(self, api_key):
        self.api_key = api_key

    async def _get_json(self, url, params: dict = None) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers={"Authorization": self.api_key}, params=params
            ) as response:
                data = await response.json()
                return data

    async def _get_buffer(self, url) -> BytesIO:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers={"Authorization": self.api_key}
            ) as response:
                return BytesIO(await response.read())

    async def my_info(self) -> dict:
        """Returns the api user's info

        Returns:
            dict: Dictionary containing user info
        """
        return await self._get_json("https://api.snowflakedev.org/api/me", {"message"})

    async def chat_bot(self, message: str, name="Bot", gender="male", user="You") -> dict:
        """AI Chatbot

        Args:
            message (str): Message you want the bot to see
            name (str, optional): Name of the Bot. Defaults to "Bot".
            gender (str, optional): Gender of the bot. Defaults to "male".
            user (str, optional): Name of the user. Defaults to "You".

        Returns:
            dict: Dictionary containing bot's response
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/chatbot",
            {"message": message, "name": name, "gender": gender, "user": user},
        )

    async def fake_discord_token(self) -> dict:
        """Fake discord bot token generator

        Returns:
            dict: Dictionary containing fake discord bot token
        """
        await self._get_json("https://api.snowflakedev.org/api/token")

    async def meme(self, sub_reddit: str = None) -> dict:
        """Random meme from a subreddit.    

        Args:
            sub_reddit (str, optional): Subreddit from which you want to fetch the meme. Defaults to None.

        Returns:
            dict: Dictionary containing meme link
        """
        if sub_reddit == None:
            return await self._get_json("https://api.snowflakedev.org/api/meme")
        else:
            return await self._get_json(
                "https://api.snowflakedev.org/api/meme", {"sbr": sub_reddit}
            )

    async def roast(self) -> dict:
        """Returns random roast.

        Returns:
            dict: Dictionary containing a random roast
        """
        return await self._get_json("https://api.snowflakedev.org/api/roast")

    async def pokemon(self, pokemon_name: str) -> dict:
        """Returns Pokemon info.

        Args:
            pokemon_name (str): Name of the pokemon

        Returns:
            dict: Dictionary containing pokemon's info
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/pokemon", {"name": pokemon_name}
        )

    async def morse_encode(self, message: str) -> dict:
        """Encode normal text into morse code

        Args:
            message (str): Text you want to encode into morse

        Returns:
            dict: Dictionary containing encoded text
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/morse/encode", {"text": message}
        )

    async def morse_decode(self, message: str) -> dict:
        """Decode morse code into normal text

        Args:
            message (str): Morse code you want to decode into normal text

        Returns:
            dict: Dictionary containing decoded text
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/morse/decode", {"text": message}
        )

    async def pypi(self, module_name: str) -> dict:
        """Python registry api

        Args:
            module_name (str): Name of the pypi module

        Returns:
            dict: Dictionary containing info about the pypi module
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/registry/pypi", {
                "module": module_name}
        )

    async def deno(self, module_name: str) -> dict:
        """Deno registry api

        Args:
            module_name (str): Name of the deno module

        Returns:
            dict: Dictionary containing info about deno module
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/registry/deno", {
                "module": module_name}
        )

    async def npm(self, module_name: str) -> dict:
        """NPM registry api

        Args:
            module_name (str): Name of the npm module

        Returns:
            dict: Dictionary containing info about npm module
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/registry/npm", {
                "module": module_name}
        )

    async def api_stats(self) -> dict:
        """Get api server stats.

        Returns:
            dict: Dictionary containing api server stats
        """
        return await self._get_json("https://api.snowflakedev.org/api/stats")

    async def githubstats(self, username: str) -> dict:
        """Returns github user stats

        Args:
            username (str): Github username

        Returns:
            dict: Dictionary containing info about the GitHub user
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/githubstats", {
                "username": username}
        )

    async def reverse(self, message: str) -> dict:
        """Reverse a message

        Args:
            message (str): Text you want to be reversed

        Returns:
            dict: Dictionary containing reversed text
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/reverse", {"message": message}
        )

    async def discord_token(self, token: str) -> dict:
        """Discord Token Information

        Args:
            token (str): Discord Token you want info about

        Returns:
            dict: Dictionary containing info about the token
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/tokeninfo", {"token": token}
        )

    async def youtube_channel(self, channel_name:str) -> dict:
        """Returns basic info about a YouTube channel

        Args:
            channel_name (str): YouTube channel you want info about

        Returns:
            dict: Dictionary containing info about the YouTube channel
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/youtube", {
                "channel": channel_name}
        )

    async def ytsearch(
        self,
        search_query: str,
        limit: int = 20,
        safesearch: bool = True,
        search_type: str = None,
    ) -> dict:
        """YouTube search

        Args:
            search_query (str): Search Query
            limit (int, optional): Number of Searches. Defaults to 20.
            safesearch (bool, optional): Boolean value for toggling SafeSearch. Defaults to True.
            search_type (str, optional): Specify whether search type is video or not. Defaults to None.

        Returns:
            dict: Dictionary containing info about Search Query from YouTube
        """
        safesearch = "1" if safesearch is None else "0"

        search_type = "video" if search_type is None else search_type

        return await self._get_json(
            "https://api.snowflakedev.org/api/ytsearch",
            {"q": search_query, "limit": limit,
                "ss": safesearch, "type": search_type},
        )

    async def base64_encode(self, text: str) -> dict:
        """Encode normal text into base64 string

        Args:
            text (str): Text you want to be encoded into Base64

        Returns:
            dict: Dictionary containing Encoded Text
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/base64/encode", {"data": text}
        )

    async def base64_decode(self, text: str) -> dict:
        """Decode base64 characters into normal text

        Args:
            text (str): Base64 you want to be decoded

        Returns:
            dict: Dictionary containing decoded Base64
        """
        return await self._get_json(
            "https://api.snowflakedev.org/api/base64/decode", {"data": text}
        )

    async def cat(self) -> BytesIO:
        """Returns random cat image.

        Returns:
            BytesIO: Returns a BytesIO object containing image of a cat
        """
        return await self._get_buffer("https://api.snowflakedev.org/api/cat")

    async def dog(self) -> BytesIO:
        """Returns random dog image.

        Returns:
            BytesIO: Returns a BytesIO object containing image of a dog
        """
        return await self._get_buffer("https://api.snowflakedev.org/api/dog")

    async def duck(self) -> BytesIO:
        """Returns random duck image.

        Returns:
            BytesIO: Returns a BytesIO object containing image of a duck
        """
        return await self._get_buffer("https://api.snowflakedev.org/api/duck")

    async def fox(self) -> BytesIO:
        """Returns random fox image.

        Returns:
            BytesIO: Returns a BytesIO object containing image of a fox
        """
        return await self._get_buffer("https://api.snowflakedev.org/api/fox")
