from backends.file_email_backend import FileEmailBackend
from backends.logging_email_backend import LoggingEmailBackend
from backends.smtp_email_backend import SmtpEmailBackend
from common import configure_logging, BASE_DIR
from email_sender import EmailSender

WELCOME_TEMPLATE = """\
Dear {name},

Welcome to our website!

Best regards,
The Team.
"""


def send_mails(sender: EmailSender) -> None:
    name = "Bob"
    recipient = "bob@ya.ru"
    subject = "Welcome to site!"
    body = "Welcome to our site!"

    sender.send(
        recipient=recipient,
        subject=subject,
        body=body,
    )

    sender.send_with_template(
        recipient=recipient,
        subject=subject,
        template=WELCOME_TEMPLATE,
        name=name,
    )


def main() -> None:
    configure_logging()

    logging_backend = LoggingEmailBackend("sender")
    sender = EmailSender(backend=logging_backend)
    send_mails(sender)

    emails_directory = BASE_DIR / "emails"
    file_backend = FileEmailBackend(directory=emails_directory)
    sender = EmailSender(backend=file_backend)
    send_mails(sender)

    smtp_backend = SmtpEmailBackend(
        smtp_server="localhost",
        smtp_port=1025,
        from_email="admin@site.ru",
    )
    sender = EmailSender(backend=smtp_backend)
    send_mails(sender)


if __name__ == "__main__":
    main()
