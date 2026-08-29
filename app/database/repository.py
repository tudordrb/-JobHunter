import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime

from app.models import Job


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "jobhunter.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def create_tables():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                fingerprint TEXT UNIQUE NOT NULL,

                title TEXT NOT NULL,
                description TEXT NOT NULL,
                platform TEXT NOT NULL,

                budget TEXT,
                url TEXT,

                discovered_at TEXT NOT NULL,

                status TEXT NOT NULL DEFAULT 'NEW',

                rejection_reason TEXT,

                final_score INTEGER
            )
            """
        )


def generate_fingerprint(job: Job, url: str = "") -> str:
    # URL-ul este cea mai bună identificare dacă îl avem.
    # Dacă lipsește, folosim titlu + descriere + platformă.
    if url:
        raw = url.strip().lower()
    else:
        raw = (
            job.platform.strip().lower()
            + "|"
            + job.title.strip().lower()
            + "|"
            + job.description.strip().lower()
        )

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()


def job_exists(job: Job, url: str = "") -> bool:
    fingerprint = generate_fingerprint(job, url)

    with get_connection() as connection:
        result = connection.execute(
            """
            SELECT id
            FROM jobs
            WHERE fingerprint = ?
            """,
            (fingerprint,),
        ).fetchone()

    return result is not None


def save_job(
    job: Job,
    budget: str = "",
    url: str = "",
) -> bool:

    fingerprint = generate_fingerprint(job, url)

    try:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO jobs (
                    fingerprint,
                    title,
                    description,
                    platform,
                    budget,
                    url,
                    discovered_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    fingerprint,
                    job.title,
                    job.description,
                    job.platform,
                    budget,
                    url,
                    datetime.now().isoformat(),
                ),
            )

        return True

    except sqlite3.IntegrityError:
        return False


def mark_rejected(
    job: Job,
    reason: str,
    url: str = "",
):
    fingerprint = generate_fingerprint(job, url)

    with get_connection() as connection:
        connection.execute(
            """
            UPDATE jobs
            SET
                status = 'REJECTED',
                rejection_reason = ?
            WHERE fingerprint = ?
            """,
            (
                reason,
                fingerprint,
            ),
        )


def mark_accepted(
    job: Job,
    url: str = "",
):
    fingerprint = generate_fingerprint(job, url)

    with get_connection() as connection:
        connection.execute(
            """
            UPDATE jobs
            SET status = 'ACCEPTED'
            WHERE fingerprint = ?
            """,
            (fingerprint,),
        )


def save_score(
    job: Job,
    score: int,
    url: str = "",
):
    fingerprint = generate_fingerprint(job, url)

    with get_connection() as connection:
        connection.execute(
            """
            UPDATE jobs
            SET
                final_score = ?,
                status = 'ANALYZED'
            WHERE fingerprint = ?
            """,
            (
                score,
                fingerprint,
            ),
        )