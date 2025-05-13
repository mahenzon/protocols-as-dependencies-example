import logging

from backends.base_email_backend import BaseEmailBackend

log = logging.getLogger(__name__)


class EmailSender:
    def __init__(
        self,
        backend: BaseEmailBackend,
    ) -> None:
        self.backend = backend

    def send(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> None:
        self.backend.send_email(recipient=recipient, subject=subject, body=body)

    def send_with_template(
        self,
        recipient: str,
        subject: str,
        template: str,
        **params,
    ) -> None:
        body = template.format(**params)
        return self.send(
            recipient=recipient,
            subject=subject,
            body=body,
        )
