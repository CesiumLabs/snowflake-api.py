import sys
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

sys.path.append("..")

from snowflakeapi import SnowClient


@pytest.mark.asyncio
async def test_api():
    api = SnowClient(os.environ.get("TOKEN"))
    message = "snowflake"
    morse = await api.morse_encode(message)

    decoded_morse = await api.morse_decode(morse["data"])
    
    assert message == str(decoded_morse["data"])
