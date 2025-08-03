# Crawlbyte Python SDK

Official Python SDK for interacting with the [Crawlbyte API](https://crawlbyte.ai).

## Features

- Create scraping tasks with various templates and configurations
- Poll task status until completion
- Retrieve task results
- Support for all Crawlbyte API parameters and options
- Type hints for better development experience

## Installation

```bash
pip install crawlbyte-sdk
# or
poetry add crawlbyte-sdk
# or
pipenv install crawlbyte-sdk
```

## Quick Start

### Initialize SDK

```python
from crawlbyte import CrawlbyteSDK

sdk = CrawlbyteSDK("your-api-key")
```

### Create and Handle Tasks

```python
# Create a task
task = sdk.create_task({
    "type": "universal",
    "input": ["https://www.walmart.com/"],
})

print(f"Task ID: {task['id']}")

# Check if task completed immediately (under 20 seconds)
if task["status"] in ["completed", "failed"]:
    print("Task completed immediately")
    print(f"Result: {task['result']}")
else:
    # If still processing, poll until completion
    result = sdk.poll_task(task["id"], {
        "interval_seconds": 5,
        "timeout_seconds": 60,
    })

    print(f"Final Status: {result['status']}")
    print(f"Result: {result['result']}")
```

### Get Task Status

```python
task = sdk.get_task("task-id")
print(f"Status: {task['status']}")
```

## Available Methods

- `create_task(payload: dict) -> dict` - Create a new scraping task. Returns results immediately if completed within 20 seconds, otherwise returns task details for polling.
- `get_task(task_id: str) -> dict` - Get task status and results.
- `poll_task(task_id: str, opts: dict) -> dict` - Poll task until completion (only needed if task takes longer than 20 seconds).

## Type Definitions

### TaskPayload Structure

```python
task_payload = {
    "type": str,                    # Required: The scraping template
    "url": str,                     # Optional: Single URL for URL-based templates
    "input": list[str],             # Optional: Array of URLs/Product IDs
    "fields": list[str],            # Optional: Specific data fields to extract
    "dataType": str,                # Optional: Type of data to extract
    "method": str,                  # Optional: HTTP method
    "jsRendering": bool,            # Optional: Enable JavaScript rendering
    "customSelector": str,          # Optional: Custom CSS selector
    "userAgentPreset": str,         # Optional: Preset user agent
    "userAgentCustom": str,         # Optional: Custom user agent
    "proxy": str,                   # Optional: Proxy configuration
    "customHeaders": dict,          # Optional: Custom HTTP headers
    "customHeaderOrder": list[str], # Optional: Order of custom headers
    "body": str,                    # Optional: Request body
    "location": str,                # Optional: Geographic location
    "sortBy": str,                  # Optional: Sort results
    "multithread": bool,            # Optional: Enable multithreading
}
```

### PollOptions Structure

```python
poll_options = {
    "interval_seconds": int,  # Polling interval in seconds
    "timeout_seconds": int,   # Total timeout in seconds
}
```

## Task Configuration

The task payload dictionary supports all Crawlbyte API parameters. Common fields include:

- `type` - The scraping template to use (e.g., "walmart", "universal")
- `input` - Array of URLs/Product IDs to scrape
- `fields` - Specific data fields to extract (sites that support this)
- `dataType` - Type of data to extract
- `jsRendering` - Enable JavaScript rendering
- `proxy` - Proxy configuration
- `customHeaders` - Custom HTTP headers

For a complete list of all available fields, configuration options, required parameters for each template, and detailed API documentation, visit: **[https://developers.crawlbyte.ai/](https://developers.crawlbyte.ai/)**

## Task Statuses

- `queued` - Task is waiting to be processed
- `processing` - Task is currently being executed
- `completed` - Task finished successfully
- `failed` - Task encountered an error

## Error Handling

The SDK raises detailed error messages for HTTP errors and API failures:

```python
try:
    task = sdk.create_task(payload)
except RuntimeError as error:
    print(f"Error creating task: {error}")
except TimeoutError as error:
    print(f"Timeout error: {error}")
```

## Examples

### Universal Template with Multiple URLs

```python
task = sdk.create_task({
    "type": "universal",
    "input": [
        "https://example1.com",
        "https://example2.com",
    ],
    "jsRendering": True,
})
```

## Environment Variables

You can set your API key as an environment variable:

```bash
export API_KEY="your-api-key"
```

Then use it in your code:

```python
import os
from crawlbyte import CrawlbyteSDK

sdk = CrawlbyteSDK(os.getenv("API_KEY"))
```

## Documentation

For comprehensive API documentation, template specifications, and field requirements, please visit:
**[https://developers.crawlbyte.ai/](https://developers.crawlbyte.ai/)**

## License

MIT
