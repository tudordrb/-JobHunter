
from datetime import datetime, timezone

from app.collectors.gmail import get_latest_freelancer_projects

from app.models import Job

from app.filters import should_reject

from app.ai.analyzer import analyze_job

from app.database.repository import (
    create_tables,
    job_exists,
    save_job,
    mark_rejected,
    mark_accepted,
    save_score,
)
print("7")
MAX_JOB_AGE_HOURS = 72


create_tables()

projects = get_latest_freelancer_projects()

for project in projects:

    email_date = project["email_date"]

    if email_date is None:
        continue

    age_hours = (
        datetime.now(timezone.utc)
        - email_date.astimezone(timezone.utc)
    ).total_seconds() / 3600

    if age_hours > MAX_JOB_AGE_HOURS:
        continue

    job = Job(
        title=project["title"],
        description=(
            project["description"]
            + "\n\nSkills: "
            + project["skills"]
        ),
        platform="Freelancer",
        remote=True,
    )

    url = project["url"]

    if job_exists(job, url):
        continue

    save_job(
        job=job,
        budget=project["budget"],
        url=url,
    )

    rejected, reason = should_reject(job)

    if rejected:
        mark_rejected(
            job,
            reason,
            url,
        )
        continue

    mark_accepted(
        job,
        url,
    )

    score = analyze_job(job)

    save_score(
        job,
        score,
        url,
    )

    if score < 75:
        continue

    print()

    print("=" * 70)

    if score >= 90:
        print(f"🟢 {score}")
    else:
        print(f"🟡 {score}")

    print()
    print(job.title)
    print()
    print(project["budget"])
    print()
    print(url)
    print()