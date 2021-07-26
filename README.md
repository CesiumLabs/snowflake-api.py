# Snowflake API

## About

This is a asynchronous python  API wrapper for [SnowFlakeAPI](https://api.snowflakedev.org/). 

## How to Use

```shell
pip install snowflakeapi
```

## Example Usage
```python
    import asyncio
    from snowflakeapi import SnowClient

    client = SnowClient("YOUR_API_KEY") # Your API Key can be found at https://api.snowflakedev.org/dashboard (sign in w/ discord)

    async def main():
        print(await client.chat_bot("hello!"))
    
    asyncio.run(main())

 ```

## API Documentation

[API Documentation](https://snowflakeapi.readthedocs.io/en/latest/)


## Want To Contribute?

You can send a pull request or open an issue to contribute.
Check out [Code Of Conduct](CODE_OF_CONDUCT.md) before contributing.
