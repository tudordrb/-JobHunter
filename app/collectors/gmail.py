import imaplib
import email
import os
import re

from dotenv import load_dotenv
from email.utils import parsedate_to_datetime


load_dotenv()


def connect_to_gmail():
    gmail_address = os.getenv("GMAIL_EMAIL")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    if not gmail_address:
        raise RuntimeError("GMAIL_EMAIL lipsește din .env")

    if not app_password:
        raise RuntimeError("GMAIL_APP_PASSWORD lipsește din .env")

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(gmail_address, app_password)
    mail.select("INBOX")

    return mail


def extract_email_body(message):
    text_body = ""

    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition", ""))

            if "attachment" in disposition.lower():
                continue

            if content_type != "text/plain":
                continue

            payload = part.get_payload(decode=True)

            if not payload:
                continue

            charset = part.get_content_charset() or "utf-8"

            try:
                text_body += payload.decode(
                    charset,
                    errors="replace"
                )
            except Exception:
                text_body += payload.decode(
                    "utf-8",
                    errors="replace"
                )

    else:
        payload = message.get_payload(decode=True)

        if payload:
            charset = message.get_content_charset() or "utf-8"

            text_body = payload.decode(
                charset,
                errors="replace"
            )

    return text_body


def normalize_freelancer_text(text):
    # Freelancer pune uneori:
    #
    # description... /projects/xyz.html?... Next Project Title
    #
    # Noi separăm URL-ul pe propria linie.

    text = re.sub(
        r"\s+(\/projects\/[^\s]+)\s+",
        r"\n\1\n",
        text
    )

    return text


def parse_projects_from_text(text):
    text = normalize_freelancer_text(text)

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    projects = []

    i = 0

    while i < len(lines):
        if not lines[i].startswith("Budget:"):
            i += 1
            continue

        title = lines[i - 1] if i > 0 else "Unknown project"

        budget = lines[i].replace(
            "Budget:",
            ""
        ).strip()

        skills = ""
        description_lines = []
        project_url = ""

        i += 1

        # -------------------------
        # SKILLS
        # -------------------------

        if i < len(lines) and lines[i].startswith("Skills:"):
            skills = lines[i].replace(
                "Skills:",
                ""
            ).strip()

            i += 1

            while i < len(lines):
                line = lines[i]

                if line.startswith("Description:"):
                    break

                skills += " " + line
                i += 1

        # -------------------------
        # DESCRIPTION
        # -------------------------

        if i < len(lines) and lines[i].startswith("Description:"):
            first_description = lines[i].replace(
                "Description:",
                ""
            ).strip()

            if first_description:
                description_lines.append(first_description)

            i += 1

            while i < len(lines):
                line = lines[i]

                # Freelancer folosește link relativ
                if line.startswith("/projects/"):
                    clean_path = line.split("?")[0]

                    project_url = (
                        "https://www.freelancer.com"
                        + clean_path
                    )

                    i += 1
                    break

                # Uneori poate exista și URL complet
                if "freelancer.com/projects/" in line:
                    match = re.search(
                        r"https?://[^\s]+",
                        line
                    )

                    if match:
                        project_url = (
                            match.group(0)
                            .split("?")[0]
                        )

                    i += 1
                    break

                # Protecție dacă apare următorul proiect
                if line.startswith("Budget:"):
                    break

                description_lines.append(line)
                i += 1

        description = " ".join(
            description_lines
        ).strip()

        projects.append(
            {
                "title": title,
                "budget": budget,
                "skills": skills,
                "description": description,
                "url": project_url,
            }
        )

    return projects


def get_latest_freelancer_projects(limit=20):
    mail = connect_to_gmail()

    try:
        status, messages = mail.search(
            None,
            '(FROM "freelancer.com")'
        )

        if status != "OK":
            raise RuntimeError(
                "Nu am putut căuta emailurile Freelancer."
            )

        email_ids = messages[0].split()

        all_projects = []

        for email_id in reversed(email_ids[-limit:]):
            status, message_data = mail.fetch(
                email_id,
                "(RFC822)"
            )

            if status != "OK":
                continue

            raw_email = message_data[0][1]

            message = email.message_from_bytes(
                raw_email
            )

            subject = message.get(
                "Subject",
                ""
            )

            # Ignorăm emailurile care nu conțin proiecte.
            if "project" not in subject.lower():
                continue

            body = extract_email_body(message)

            projects = parse_projects_from_text(
                body
            )

            email_date_raw = message.get(
                "Date",
                ""
            )

            try:
                email_date = parsedate_to_datetime(
                    email_date_raw
                )

            except Exception:
                email_date = None

            for project in projects:
                project["email_id"] = (
                    email_id.decode()
                )

                project["email_date"] = (
                    email_date
                )

                all_projects.append(project)

        return all_projects

    finally:
        try:
            mail.logout()
        except Exception:
            pass