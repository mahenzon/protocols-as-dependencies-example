import logging

from backends.base_email_backend import BaseEmailBackend


class LoggingEmailBackend(BaseEmailBackend):
    def __init__(self, name: str) -> None:
        self.log = logging.getLogger(name)

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> None:
        self.log.info(
            "Sending email to %r with subject %r and body %r",
            recipient,
            subject,
            body,
        )
