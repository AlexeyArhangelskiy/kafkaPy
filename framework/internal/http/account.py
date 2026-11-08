import httpx

from framework.internal.http.log import log_response

class AccountApi:
    def __init__(self, base_url: str = "http://185.185.143.231:8085", timeout: float = 10.0) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            event_hooks={"response": [log_response]},
        )

    def register_user(self, login: str, email: str, password: str) -> httpx.Response:
        data = {
            "login": login,
            "email": email,
            "password": password,
        }
        response =  self._client.post(
            "/register/user/async-register",
            json=data,
        )
        return response