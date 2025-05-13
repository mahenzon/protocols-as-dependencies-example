import random
from datetime import datetime
from pathlib import Path

from backends.base_email_backend import BaseEmailBackend


class FileEmailBackend(BaseEmailBackend):
    def __init__(
        self,
        directory: Path,
    ) -> None:
        self.directory = directory
        self.directory.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_filename(
        cls,
        recipient: str,
        subject: str,
    ) -> str:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        rnd = random.randint(1_000_000, 9_999_999)
        rec = recipient.replace("@", "_at_")
        subj = subject.replace(" ", "_")
        return f"{ts}.{rnd}._{rec}_{subj}.txt"

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> None:
        filename = self.get_filename(
            recipient=recipient,
            subject=subject,
        )
        filepath = self.directory / filename

        with filepath.open("w") as f:
            f.write(f"To: {recipient}\n")
            f.write(f"Subject: {subject}\n\n")
            f.write(body)
