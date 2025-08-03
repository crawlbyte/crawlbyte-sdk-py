import os
import pytest
from crawlbyte.sdk import CrawlbyteSDK
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def test_create_task(): 
    sdk = CrawlbyteSDK(API_KEY)
    task = sdk.create_task({ 
        "type": "universal",
        "input": ["https://example.com"]
    })
    assert "id" in task
