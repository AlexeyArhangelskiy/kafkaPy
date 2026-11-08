import httpx

from framework.internal.http.log import log_response

class MailApi:
    def __init__(self, base_url: str = "http://185.185.143.231:8085", timeout: float = 10.0) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            event_hooks={"response": [log_response]},
        )

    def mail_search(self, query: str) -> httpx.Response:
        params = {
            "query": query,
            "limit": 1,
            "kind": "containing",
            "start": 0,
        }
        response =  self._client.get(
            "/mail/mail/search",
            params=params,
        )
        return response
