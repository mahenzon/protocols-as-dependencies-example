from backends.smtp_email_backend import SmtpEmailBackend
from backends.logging_email_backend import LoggingEmailBackend
from backends.file_email_backend import FileEmailBackend
from common import configure_logging, BASE_DIR
from email_sender import EmailSender

welcome_template = """\
Dear {name},

Welcome to our site!

Best regards,
The Team.
"""


def send_emails(sender: EmailSender) -> None:
    recipient = "bob@ya.ru"
    subject = "Welcome Message"
    body = "Dear user, thank you for registering!"

    sender.send(
        recipient=recipient,
        subject=subject,
        body=body,
    )

    sender.send_with_template(
        recipient=recipient,
        subject=subject,
        template=welcome_template,
        name="John",
    )


def main() -> None:
    configure_logging()
    logging_backend = LoggingEmailBackend("sender")
    sender = EmailSender(backend=logging_backend)
    send_emails(sender)

    emails_path = BASE_DIR / "emails"

    file_backend = FileEmailBackend(directory=emails_path)
    sender = EmailSender(backend=file_backend)
    send_emails(sender)

    smtp_backend = SmtpEmailBackend(
        smtp_server="localhost",
        smtp_port=1025,
        from_email="admin@internet.ru",
    )
    sender = EmailSender(backend=smtp_backend)
    send_emails(sender)


if __name__ == "__main__":
    main()
