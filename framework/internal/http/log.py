import json
import logging

import httpx

logger = logging.getLogger("http")

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("kafka").setLevel(logging.WARNING)


def log_response(response: httpx.Response) -> None:
    response.read()
    request = response.request
    try:
        body = json.dumps(response.json(), ensure_ascii=False, indent=2)
    except ValueError:
        body = response.text
    logger.info("%s %s -> %s\n%s", request.method, request.url, response.status_code, body)
