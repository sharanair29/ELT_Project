from dagster import ScheduleDefinition, DefaultScheduleStatus
from ..jobs import jobs


profile_schedule = ScheduleDefinition(
    job=jobs.extract_profile_job,
    cron_schedule="0 0 * * 0",
    default_status=DefaultScheduleStatus.RUNNING,
)

company_schedule = ScheduleDefinition(
    job=jobs.extract_company_job,
    cron_schedule="0 0 1 * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
