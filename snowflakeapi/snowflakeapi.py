import requests

class SnowClient:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY;

    def myInfo(self):
        # Fetch your account in JSON format
        return requests.get("https://api.snowflakedev.org/api/me", headers={'Authorization': self.API_KEY}).json()

    def chatBot(self, message: str, name = "Bot", gender = "male", user = "You"):
        # If statement checking what values exist
        if (message == None): return print("Error - No Message Provided")

        # Get a message from the chatbot
        return requests.get("https://api.snowflakedev.org/api/chatbot", params={'message': message, 'name': name, 'gender': gender, 'user': user}, headers={'Authorization': self.API_KEY}).json()
        
    def fakeDiscordToken(self):
        # Generate a fake token
        return requests.get("https://api.snowflakedev.org/api/token", headers={'Authorization': self.API_KEY}).json()

    def meme(self, subReddit = None): 
        # Get a random meme from the specified subreddit
        if (subReddit == None):
            return requests.get("https://api.snowflakedev.org/api/meme", headers={'Authorization': self.API_KEY}).json()
        else:
            return requests.get("https://api.snowflakedev.org/api/meme", params={'sbr': subReddit}, headers={'Authorization': self.API_KEY}).json()

    def roast(self):
        # Get a roast
        return requests.get("https://api.snowflakedev.org/api/roast", headers={'Authorization': self.API_KEY}).json()

    def pokemon(self, pokemonName):
        # Get information about x pokemon, as well as the image
        return requests.get("https://api.snowflakedev.org/api/pokemon", params={'name': pokemonName}, headers={'Authorization': self.API_KEY}).buffer    

    def morse(self, type: str, message: str):
        # Convert a message to morse code
        if (type == None): return print("Error - No Type Provided")
        if (message == None): return print("Error - No Message Provided")

        if (type == "encode"):
            return requests.get("https://api.snowflakedev.org/api/morse/encode", params={'text': message}, headers={'Authorization': self.API_KEY}).json()
        elif (type == "decode"):
            return requests.get("https://api.snowflakedev.org/api/morse/decode", params={'text': message}, headers={'Authorization': self.API_KEY}).json()
        else:
            return print("Error - Invalid Type")

    def registry(self, registryName, moduleName):
        # Get a package from the registry
        if (registryName == None): return print("Error - No Registry Provided")
        if (moduleName == None): return print("Error - No Module Provided")

        if (registryName == "deno"):
            return requests.get("https://api.snowflakedev.org/api/registry/deno", params={'module': moduleName}, headers={'Authorization': self.API_KEY}).json()
        elif (registryName == "npm"):
            return requests.get("https://api.snowflakedev.org/api/registry/npm", params={'module': moduleName}, headers={'Authorization': self.API_KEY}).json()
        elif (registryName == "pypi"):
            return requests.get("https://api.snowflakedev.org/api/registry/pypi", params={'module': moduleName}, headers={'Authorization': self.API_KEY}).json()
        else: 
            return print("Error - Invalid Registry | Valid: deno, npm, pypi")

    def apiStats(self):
        # Get information about the API
        return requests.get("https://api.snowflakedev.org/api/stats", headers={'Authorization': self.API_KEY}).json()     

    def githubstats(self, username: str):
        # Get information about a GitHub user
        if (username == None): return print("Error - No Username Provided")

        return requests.get("https://api.snowflakedev.org/api/githubstats", params={'username': username}, headers={'Authorization': self.API_KEY}).json()       

    def reverse(self, message: str):
        # Reverse a message
        if (message == None): return print("Error - No Message Provided")

        return requests.get("https://api.snowflakedev.org/api/reverse", params={'message': message}, headers={'Authorization': self.API_KEY}).json()

    def discordTokenInfo(self, token: str):
        # Get information about a Discord token
        if (token == None): return print("Error - No Token Provided")

        return requests.get("https://api.snowflakedev.org/api/tokeninfo", params={'token': token}, headers={'Authorization': self.API_KEY}).json()    

    def youtubeChannel(self, channelName):
        # Get information about a YouTube channel
        if (channelName == None): return print("Error - No Channel Provided")

        return requests.get("https://api.snowflakedev.org/api/youtube", params={'channel': channelName}, headers={'Authorization': self.API_KEY}).json()    

    def ytsearch(self, searchQuery: str, limit: int = 20, safesearch: bool = True, type: str = None):
        # Search YouTube
        if (searchQuery == None): return print("Error - No Search Query Provided")

        if (safesearch == None):
            safesearch = "1"
        else:
            safesearch = "0"

        if (type == None):
            type = "video"
        else:
            type = type

        return requests.get("https://api.snowflakedev.org/api/youtube/search", params={'searchQuery': searchQuery, 'limit': limit, 'ss': safesearch, 'type': type}, headers={'Authorization': self.API_KEY}).json()

    def base64(self, type: str, text: str):
        # Encode a string to base64
        if (type == None): return print("Error - No Type Provided")
        if (text == None): return print("Error - No Message Provided")

        if (type == "encode"):
            return requests.get("https://api.snowflakedev.org/api/base64/encode", params={'data': text}, headers={'Authorization': self.API_KEY}).json()
        elif (type == "decode"):
            return requests.get("https://api.snowflakedev.org/api/base64/decode", params={'data': text}, headers={'Authorization': self.API_KEY}).json()
        else:
            return print("Error - Invalid Type")

    def cat(self):
        # Get a random cat image
        return requests.get("https://api.snowflakedev.org/api/cat", headers={'Authorization': self.API_KEY}).buffer

    def dog(self):
        # Get a random dog image
        return requests.get("https://api.snowflakedev.org/api/dog", headers={'Authorization': self.API_KEY}).buffer

    def duck(self):
        # Get a random duck image
        return requests.get("https://api.snowflakedev.org/api/duck", headers={'Authorization': self.API_KEY}).buffer

    def fox(self):
        # Get a random fox image
        return requests.get("https://api.snowflakedev.org/api/fox", headers={'Authorization': self.API_KEY}).buffer