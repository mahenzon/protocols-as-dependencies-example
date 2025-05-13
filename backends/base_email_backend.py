from typing import Protocol


class BaseEmailBackend(Protocol):

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> None: ...
