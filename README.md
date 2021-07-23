# Snowflake API

### Example Usage
```python
    from snowflakeapi.snowflakeapi import SnowClient
    client = SnowClient("YOUR_API_KEY") # Your API Key can be found at https://api.snowflakedev.org/dashboard (sign in w/ discord)

    print(client.chatbot("hello!"))
 ```

### API Documentation

## myInfo()
Used to fetch your API Profile Information
```python
    client.myInfo()
```
### Response
```
{ user, pro, ratelimits, banned, requests, tokenCreatedTimestamp, createdTimestamp }
```
---
## chatBot(message, name, gender, user)
Talk to a chatbot

**name, gender and user params are optional**

```python
    message = input("Your message/question:")
    client.chatBot(message, "Chatty", "male", "You")
```
### Response
```
{ message }
```
---
## fakeDiscordToken()
Generate a fake discord token
```python
    client.fakeDiscordToken()
```
### Response
```
{ token }
```    
---
# meme(subreddit)
Get a random meme, either from a specific subreddit or a random one

**subreddit paramater is optional**

```python
    subreddit = input("Subreddit: ")
    client.meme(subreddit)
```

### Response
```
{ isVideo, nsfw, createdAt, url, ratings: { upvote, downvote, comments }, subreddit, title, link }
```

# roast()
Get a random roast!
```python
    client.roast()
```
### Response
```
    { roast }
```
---
# pokemon(pokemonName)
Fetch information about a specific pokemon!
```python
    pokemonName = input("Pokemon Name: ")
    client.pokemon(pokemonName)
```

### Response
```
    { name, id, baseExperience, height, weight, type, moves, stats, image }
```
---
# morse(type, message)
Encode/Decode a message
```python
# Endode
client.morse("encode", "Hello")

# Decode
client.morese("decode", ".... . .-.. .-.. ---")
```

### Response
```
{ data }
```
---

# registery 
Fetch data about a module from deno, npm or pypi.
```python
# Deno 
client.registry("deno", "youtube-sr")

# NPM
client.registry("npm", "youtube-sr")

# PyPi
client.registry("pypi", "snowflakeapi")
```

### Responses
```
 // Deno
{ registry, icon, url, module: { name, url, description, version, stars, developer: { name, url }, github, createdAt } }

// NPM 
{ registry, icon, url, runkit, module: { name, url, description, version, main, license, author, maintainers, dependencies, repository, banner } }

// PyPi
{ registry, icon, url, module: { name, description, url, version, author, updatedAt, documentation, homepage }
```
---
# apiStats()
Get statisticle information about SnowflakeDev API
```python
    client.apiStats()
```

### Response
```
{ total_requests, free_users, pro_users, total_users, banned_users, os, processor: { model, count }, memory: { heap_total, heap_used, rss, external, ab } }
```
---
# githubstats(username)
Get information about a github profile.
```python
    client.githubstats("DevSynth")
```
### Response
```
{ name, avatar, followers, repos, pullRequests, issues, npmDownloads }
```
---
# reverse(message)
Reverse any text!
```python
    client.reverse("Hello, how are you?")
```
### Response
```
{ message }
```
---
# discordTokenInfo(token)
Get information about a discord token (TOKENS ARE NOT SAVED)
```python
    client.discordTokenInfo("TOKEN_HERE")
```
### Response
```
{ type, token, id, username, discriminator, avatar, avatarURL, snowflakeInfo }
```
---
# youtubeChannel(channel)
Get information about a youtube channel
```python
    client.youtubeChannel("Channel Name")
```
### Response
```
{ channel: { name, url }, videos: [ { id, title, author, url, publishedAt, thumbnail }, ... ] }
```
---
#  ytSearch(searchQuery, limit, safesearch, type)
Get information about a youtube video
```python
    client.ytSearch("Hello", 1, True, "video")
```
### Response
```
{ data: [...] }
```
---
# base64(type, message)
Encode/Decode a message
```python
# Encode
client.base64("encode", "Hello")

# Decode
client.base64("decode", "SGVsbG8K")
```
### Response
```
{ data }
```
---
# cat(), dog(), duck(), fox()
Get a random image of cats, dogs, ducks, or fox's.
```python
    client.cat()
    client.dog()
    client.fox()
    client.duck()
```
### Response
```
{ IMAGE_BUFFER }
```
